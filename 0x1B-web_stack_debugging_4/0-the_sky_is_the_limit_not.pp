# A benchmark for web server setup featuring Nginx is doing under pressure 

package { 'nginx':
  ensure => installed,
}

file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => template('nginx/nginx.conf.erb'),
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  hasstatus => true,
  hasrestart=> true,
  require   => Package['nginx'],
}
class { 'nginx_config': }
