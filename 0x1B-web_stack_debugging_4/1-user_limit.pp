#Change the OS configuration  enable login with the holberton user and open a file without any error message.
file { '/etc/security/limits.d/holberton.conf':
  ensure  => present,
  content => "holberton soft nofile 4096\nholberton hard nofile 8192\n",
}

exec { 'reload_limits':
  command => 'pkill -u holberton -SIGHUP',
  path    => '/usr/bin',
  user    => 'root',
  require => File['/etc/security/limits.d/holberton.conf'],
}
