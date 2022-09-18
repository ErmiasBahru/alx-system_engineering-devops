# Puppet to make changes to our configuration file

file_line {'PasswordAuthentication ':
  path  => '/etc/ssh/ssh_config',
  line  => 'PasswordAuthentication ',
  match => 'PasswordAuthentication no'
}

file_line {'IdentityFile ':
  path  => '/etc/ssh/ssh_config',
  line  => 'IdentityFile ',
  match => 'IdentityFile ~/.ssh/school'
}
