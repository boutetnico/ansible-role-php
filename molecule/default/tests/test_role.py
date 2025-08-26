import re

PHP_VERSION = "8.4"


def test_repo_exists(host):
    distro = host.system_info.distribution.lower()
    if "debian" in distro:
        f = host.file("/etc/apt/sources.list.d/sury.sources")
        assert f.exists and f.is_file
        assert "packages.sury.org/php" in f.content_string


def test_php_package_installed(host):
    pkg = host.package(f"php{PHP_VERSION}-fpm")
    assert pkg.is_installed


def assert_ini_kv(content: str, key: str, value: str):
    pattern = rf"(?m)^\s*{re.escape(key)}\s*=\s*{re.escape(value)}\s*$"
    assert re.search(pattern, content)


def test_php_cli_ini_exists(host):
    f = host.file(f"/etc/php/{PHP_VERSION}/cli/php.ini")
    assert f.exists and f.is_file
    c = f.content_string

    assert_ini_kv(c, "engine", "On")
    assert_ini_kv(c, "expose_php", "Off")
    assert_ini_kv(c, "error_reporting", "E_ALL")
    assert_ini_kv(c, "html_errors", "Off")
    assert_ini_kv(c, "display_errors", "Off")
    assert_ini_kv(c, "display_startup_errors", "Off")
    assert_ini_kv(c, "error_log", "syslog")
    assert_ini_kv(c, "log_errors", "On")
    assert_ini_kv(c, "date.timezone", "UTC")
    assert_ini_kv(c, "default_charset", '"UTF-8"')
    assert_ini_kv(c, "file_uploads", "On")
    assert_ini_kv(c, "upload_max_filesize", "2M")
    assert_ini_kv(c, "post_max_size", "8M")
    assert_ini_kv(c, "max_file_uploads", "20")
    assert_ini_kv(c, "session.save_handler", "files")
    assert_ini_kv(c, "session.gc_divisor", "100")
    assert_ini_kv(c, "session.gc_probability", "1")
    assert_ini_kv(c, "session.gc_maxlifetime", "1440")
    assert_ini_kv(c, "session.cookie_lifetime", "0")
    assert_ini_kv(c, "session.upload_progress.enabled", "On")
    assert_ini_kv(c, "session.upload_progress.cleanup", "On")
    assert_ini_kv(c, "session.cookie_secure", "On")
    assert_ini_kv(c, "session.cookie_httponly", "On")
    assert_ini_kv(c, "session.cookie_samesite", "Lax")
    assert_ini_kv(c, "opcache.enable", "On")
    assert_ini_kv(c, "opcache.enable_cli", "Off")
    assert_ini_kv(c, "opcache.memory_consumption", "128")
    assert_ini_kv(c, "opcache.interned_strings_buffer", "8")
    assert_ini_kv(c, "opcache.max_accelerated_files", "10000")
    assert_ini_kv(c, "opcache.revalidate_freq", "2")
    assert_ini_kv(c, "opcache.validate_timestamps", "On")


def test_php_fpm_ini_exists(host):
    f = host.file(f"/etc/php/{PHP_VERSION}/fpm/php.ini")
    assert f.exists and f.is_file


def test_php_fpm_pool_managed(host):
    f = host.file(f"/etc/php/{PHP_VERSION}/fpm/pool.d/www.conf")
    assert f.exists and f.is_file
    c = f.content_string
    assert "; Ansible managed" in c
    assert "pm = dynamic" in c
    assert "pm.status_path = /php_status/www" in c
    assert "ping.path = /php_ping/www" in c


def test_php_fpm_conf_log_level(host):
    f = host.file(f"/etc/php/{PHP_VERSION}/fpm/php-fpm.conf")
    assert f.exists and f.is_file
    assert "log_level = warning" in f.content_string


def test_systemd_override_installed(host):
    d = host.file(f"/etc/systemd/system/php{PHP_VERSION}-fpm.service.d")
    assert d.exists and d.is_directory
    f = host.file(f"/etc/systemd/system/php{PHP_VERSION}-fpm.service.d/override.conf")
    assert f.exists and f.is_file


def test_php_cli_binary(host):
    cmd = host.run("php -v")
    assert cmd.rc == 0


def test_php_fpm_service_running_enabled(host):
    svc = host.service(f"php{PHP_VERSION}-fpm")
    assert svc.is_enabled
    assert svc.is_running


def test_fpm_socket_exists(host):
    s = host.socket(f"unix:///run/php/php{PHP_VERSION}-fpm.sock")
    assert s.is_listening
