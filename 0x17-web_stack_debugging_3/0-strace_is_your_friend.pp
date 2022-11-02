# Using strace, find out why Apache
# is returning a 500 error.

exec {'Fixer':
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
  path    => '/usr/bin/:/usr/local/bin/:/bin/'
}
