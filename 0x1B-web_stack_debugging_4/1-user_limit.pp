# Change the OS configuration so that it is possible to login with the holberton user and open a file without any error message.

class user_limits {

  exec { 'set_holberton_limits':
    command => '/bin/su - holberton -c "ulimit -n 65535"',
    path    => '/bin:/usr/bin',
  }
}

class { 'user_limits': }

