[![tests](https://github.com/boutetnico/ansible-role-php/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-php/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.php-blue.svg)](https://galaxy.ansible.com/boutetnico/php)

ansible-role-php
================

This role installs [PHP](https://www.php.net/).

Requirements
------------

Ansible 2.10 or newer.

Supported Platforms
-------------------

- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Debian - 12 (Bookworm)](https://wiki.debian.org/DebianBookworm)
- [Ubuntu - 22.04 (Jammy Jellyfish)](http://releases.ubuntu.com/22.04/)
- [Ubuntu - 24.04 (Noble Numbat)](http://releases.ubuntu.com/24.04/)

Role Variables
--------------

| Variable                            | Required | Default   | Choices         | Comments                              |
|-------------------------------------|----------|-----------|-----------------|---------------------------------------|
| php_version                         | true     | `"8.4"`   | string          | PHP major.minor version               |
| php_dependencies                    | true     |           | list            | See `defaults/main.yml`               |
| php_packages                        | true     |           | list            | See `defaults/main.yml`               |
| php_extra_packages                  | true     | `[]`      | list            | Additional PHP packages               |
| php_packages_state                  | true     | `present` | present/absent  | State of PHP packages                 |
| php_pear_packages                   | true     | `[]`      | list            | PEAR packages                         |
| php_pear_packages_state             | true     | `present` | present/absent  | State of PEAR packages                |
| php_extensions                      | true     | `[]`      | list(dict)      | Extra extensions with config          |
| php_engine                          | true     | `true`    | bool            | Enable PHP engine                     |
| php_expose_php                      | true     | `false`   | bool            | Expose PHP via headers                |
| php_max_execution_time              | true     | `30`      | int             | Script execution time in seconds      |
| php_memory_limit                    | true     | `128M`    | string          | Memory limit                          |
| php_default_socket_timeout          | true     | `60`      | int             | Socket timeout in seconds             |
| php_error_reporting                 | true     | `E_ALL`   | string          | Error reporting level                 |
| php_html_errors                     | true     | `false`   | bool            | Use HTML formatting for errors        |
| php_display_errors                  | true     | `false`   | bool            | Display errors                        |
| php_display_startup_errors          | true     | `false`   | bool            | Display startup errors                |
| php_error_log                       | true     | `syslog`  | string          | Error log path or `syslog`            |
| php_log_errors                      | true     | `true`    | bool            | Log errors                            |
| php_date_timezone                   | true     | `UTC`     | string          | Timezone                              |
| php_default_charset                 | true     | `UTF-8`   | string          | Default charset                       |
| php_file_uploads                    | true     | `true`    | bool            | Enable file uploads                   |
| php_upload_max_filesize             | true     | `2M`      | string          | Max upload size                       |
| php_post_max_size                   | true     | `8M`      | string          | Max POST size                         |
| php_max_file_uploads                | true     | `20`      | int             | Max uploaded files per request        |
| php_session_save_handler            | true     | `files`   | string          | Session handler                       |
| php_session_save_path               | true     | `""`      | string          | Session save path                     |
| php_session_gc_divisor              | true     | `100`     | int             | Session GC divisor                    |
| php_session_gc_probability          | true     | `1`       | int             | Session GC probability                |
| php_session_gc_maxlifetime          | true     | `1440`    | int             | Session max lifetime (s)              |
| php_session_cookie_lifetime         | true     | `0`       | int             | Session cookie lifetime (s)           |
| php_session_upload_progress_enabled | true     | `true`    | bool            | Enable upload progress                |
| php_session_upload_progress_cleanup | true     | `true`    | bool            | Cleanup upload progress data          |
| php_session_cookie_secure           | true     | `true`    | bool            | Secure session cookies (HTTPS)        |
| php_session_cookie_httponly         | true     | `true`    | bool            | HttpOnly session cookies              |
| php_session_cookie_samesite         | true     | `Lax`     | string          | Session SameSite policy               |
| php_opcache_enable                  | true     | `true`    | bool            | Enable opcache                        |
| php_opcache_enable_cli              | true     | `false`   | bool            | Enable opcache in CLI                 |
| php_opcache_memory_consumption      | true     | `128`     | int             | Opcache memory size (MB)              |
| php_opcache_interned_strings_buffer | true     | `8`       | int             | Opcache interned strings buffer       |
| php_opcache_max_accelerated_files   | true     | `10000`   | int             | Opcache max accelerated files         |
| php_opcache_revalidate_freq         | true     | `2`       | int             | Opcache revalidate frequency          |
| php_opcache_validate_timestamps     | true     | `true`    | bool            | Validate opcache timestamps           |
| php_fpm_log_level                   | true     | `warning` | string          | FPM log level                         |
| php_fpm_pools                       | true     |           | list(dict)      | See `defaults/main.yml`               |
| php_extra_ini                       | true     | `{}`      | dict            | Extra ini settings (key/value pairs)  |
| php_fpm_systemd_override            | true     |           | dict            | See `defaults/main.yml`               |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - role: ansible-role-php

Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
