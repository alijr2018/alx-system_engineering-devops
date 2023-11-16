# Description: Puppet manifest to modify Nginx configuration and restart service

# Update the configuration in /etc/default/nginx
exec { 'modify_nginx_config':
  command => '/usr/bin/env sed -i s/15/1000/ /etc/default/nginx',
  path    => '/bin:/usr/bin',
  notify  => Exec['restart_nginx'],
}

# Restart the Nginx service after modifying the config
exec { 'restart_nginx':
  command     => '/usr/bin/env service nginx restart',
  path        => '/sbin:/usr/sbin:/bin:/usr/bin',
  refreshonly => true,
}

# Define relationships between tasks
Exec['modify_nginx_config'] -> Exec['restart_nginx']

