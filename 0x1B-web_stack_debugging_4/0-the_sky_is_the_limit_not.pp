# Increase the amount of trafix on the nginx server

# Increase the ULIMIT of the default file
exec { 'fix--for-nginx':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
}


# Restart nginx
exec {'nginx-restart':
  # restart nginx service
  command => '/etc/init.d/nginx restart',
  # specify the path for the init.d script
  path    => '/etc/init.d/',
}
