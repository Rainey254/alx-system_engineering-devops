#Puppet file that fixes multiple server errors in Nginx serverr

exec { 'fix_limit':
  path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command  =>  "sed -i 's/ULIMIT=\"-n 15\"/ULIMIT=\"-n 3072\"/g' /etc/default/nginx; sudo service nginx restart",
  provider => 'shell'}
