# 101-setup_web_static.pp
# Puppet manifest to set up the web static structure

# Ensure the /data directory exists
file { '/data':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

# Ensure the web_static directory exists
file { '/data/web_static':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

# Ensure the releases directory exists
file { '/data/web_static/releases':
  ensure => directory,
  owner  => 'root',
  group  => 'root',
  mode   => '0755',
}

# Ensure the shared directory exists
file { '/data/web_static/shared':
  ensure => directory,
  owner  => 'root',
  group  => 'root',
  mode   => '0755',
}

# Ensure the test release directory exists
file { '/data/web_static/releases/test':
  ensure => directory,
  owner  => 'root',
  group  => 'root',
  mode   => '0755',
}

# Ensure the index.html file exists in the test release
file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => '<html>
  <head>
  </head>
  <body>
    ALX
  </body>
</html>',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

# Create a symbolic link from /data/web_static/current to the test release
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
}

# Ensure the Nginx configuration serves the /hbnb_static path
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('/path/to/nginx/default.erb'), # Replace with the correct template path
  notify  => Service['nginx'],
}

# Ensure the Nginx service is running and enabled
service { 'nginx':
  ensure => running,
  enable => true,
}
