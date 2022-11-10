# Changes /etc/default/nginx file to increase limit
# current nginx request open files

exec {'Increase nginx limit':
  command => "sed -i 's/15/10000/' /etc/default/nginx; sudo service nginx restart",
  path    => '/usr/bin/:/usr/local/bin/:/bin/'
}
