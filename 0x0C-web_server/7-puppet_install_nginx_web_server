#!/usr/bin/env bash
# Configure Nginx server using puppet

# Puppet class called that encapsulates the
# configuration for the Nginx server.
class nginxserver {
  package { 'nginx':
    ensure => installed,
  }

#  Manages the Nginx service.
  service { 'nginx':
    enable => true,
    require => Package['nginx'],
    ensure => running,
  }
# Manages the Nginx configuration file located at /etc/nginx/sites-available/default.
  file { '/etc/nginx/sites-available/default':
    ensure  => present,
    content => "
      server {
        listen      80 default_server;
        listen      [::]:80 default_server;
        index       index.html index.htm;
        root        /var/www/html;

        location / {
          return 200 'Hello World!';
        }

        location /redirect_me {
          return 301 http://cuberule.com/;
        }
      }
    ",
    notify => Service['nginx'],
  }
}

include nginxserver
