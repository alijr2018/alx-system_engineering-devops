# A benchmark for web server setup featuring Nginx is doing under pressure

exec { 'modify_nginx_config':
  command => '/usr/bin/env sed -i s/15/1000/ /etc/default/nginx',
  path    => '/bin:/usr/bin',
  notify  => Exec['restart_nginx'],
}

exec { 'restart_nginx':
  command     => '/usr/bin/env service nginx restart',
  path        => '/sbin:/usr/sbin:/bin:/usr/bin',
  refreshonly => true,
}

Exec['modify_nginx_config'] -> Exec['restart_nginx']

