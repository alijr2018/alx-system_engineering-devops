# Change the OS configuration so that it is possible to login with the holberton user and open a file without any error message.

exec { 'change_limits_conf':
  command => '/usr/bin/env sed -i "s/holberton/foo/" /etc/security/limits.conf',
  path    => '/usr/bin:/bin',
}

