# Puppet setup to connect to server without password
include stdlib

file { 'Turn off passwd auth':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '	PasswordAuthentication no',
  replace => true,
}

file { 'Declare identity file':
  ensure  => present,
  path    => /etc/ssh/ssh_config,
  line    => '	IdentityFile ~/.ssh/school',
  replace => true,
}
