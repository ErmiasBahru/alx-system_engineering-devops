# to login with the holberton user and open a file without any error message.
file { 'loginFile':
    ensure  => present,
    path    => '/etc/security/limits.conf',
    content => '#File erased'
}
