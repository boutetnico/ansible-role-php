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

| Variable                          | Required | Default   | Choices         | Comments                              |
|-----------------------------------|----------|-----------|-----------------|---------------------------------------|
| php_version                       | true     | `"8.4"`   | string          | PHP major.minor version               |
| php_dependencies                  | false    |           | list            | See `defaults/main.yml`               |
| php_packages                      | false    |           | list            | See `defaults/main.yml`               |
| php_extra_packages                | false    | `[]`      | list            | Additional PHP packages               |
| php_packages_state                | false    | `present` | present/absent  | State of PHP packages                 |
| php_pear_packages                 | false    | `[]`      | list            | PEAR packages                         |
| php_pear_packages_state           | false    | `present` | present/absent  | State of PEAR packages                |
| php_extensions                    | false    | `[]`      | list(dict)      | Extra extensions with config          |
| php_engine                        | false    | `true`    | bool            | Enable PHP engine                     |
| php_expose_php                    | false    | `false`   | bool            | Expose PHP via headers                |
| php_max_execution_time            | false    | `30`      | int             | Script execution time in seconds      |
| php_memory_limit                  | false    | `128M`    | string          | Memory limit                          |
| php_default_socket_timeout        | false    | `60`      | int             | Socket timeout in seconds             |
| php_error_reporting               | false    | `E_ALL`   | string          | Error reporting level                 |
| php_html_errors                   | false    | `false`   | bool            | Use HTML formatting for errors        |
| php_display_errors                | false    | `false`   | bool            | Display errors                        |
| php_display_startup_errors        | false    | `false`   | bool            | Display startup errors                |
| php_error_log                     | false    | `syslog`  | string          | Error log path or `syslog`            |
| php_log_errors                    | false    | `true`    | bool            | Log errors                            |
| php_date_timezone                 | false    | `UTC`     | string          | Timezone                              |
| php_default_charset               | false    | `UTF-8`   | string          | Default charset                       |
| php_file_uploads                  | false    | `true`    | bool            | Enable file uploads                   |
| php_upload_max_filesize           | false    | `2M`      | string          | Max upload size                       |
| php_post_max_size                 | false    | `8M`      | string          | Max POST size                         |
| php_max_file_uploads              | false    | `20`      | int             | Max uploaded files per request        |
| php_session_save_handler          | false    | `files`   | string          | Session handler                       |
| php_session_save_path             | false    | `""`      | string          | Session save path                     |
| php_session_gc_divisor            | false    | `100`     | int             | Session GC divisor                    |
| php_session_gc_probability        | false    | `1`       | int             | Session GC probability                |
| php_session_gc_maxlifetime        | false    | `1440`    | int             | Session max lifetime (s)              |
| php_session_cookie_lifetime       | false    | `0`       | int             | Session cookie lifetime (s)           |
| php_session_upload_progress_enabled | false  | `true`    | bool            | Enable upload progress                |
| php_session_upload_progress_cleanup | false  | `true`    | bool            | Cleanup upload progress data          |
| php_session_cookie_secure         | false    | `true`    | bool            | Secure session cookies (HTTPS)        |
| php_session_cookie_httponly       | false    | `true`    | bool            | HttpOnly session cookies              |
| php_session_cookie_samesite       | false    | `Lax`     | string          | Session SameSite policy               |
| php_opcache_enable                | false    | `true`    | bool            | Enable opcache                        |
| php_opcache_enable_cli            | false    | `false`   | bool            | Enable opcache in CLI                 |
| php_opcache_memory_consumption    | false    | `128`     | int             | Opcache memory size (MB)              |
| php_opcache_interned_strings_buffer | false  | `8`       | int             | Opcache interned strings buffer       |
| php_opcache_max_accelerated_files | false    | `10000`   | int             | Opcache max accelerated files         |
| php_opcache_revalidate_freq       | false    | `2`       | int             | Opcache revalidate frequency          |
| php_opcache_validate_timestamps   | false    | `true`    | bool            | Validate opcache timestamps           |
| php_fpm_log_level                 | false    | `warning` | string          | FPM log level                         |
| php_fpm_pools                     | false    |           | list(dict)      | See `defaults/main.yml`               |
| php_extra_ini                     | false    | `{}`      | dict            | Extra ini settings (key/value pairs)  |
| php_fpm_systemd_override          | false    |           | dict            | See `defaults/main.yml`               |

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
