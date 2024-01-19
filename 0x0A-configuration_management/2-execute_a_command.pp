# kills a process named killmenow

exec { 'killmenow':
  command     => '/usr/bin/pkill -f killmenow',
  onlyif      => '/usr/bin/pgrep -f killmenow',
  refreshonly => true,
  logoutput   => true,
  subscribe   => File['/alx-system_engineering-devops/0x0A-configuration_management/killmenow'],
}

file { '/alx-system_engineering-devops/0x0A-configuration_management/killmenow':
  ensure  => file,
  content => "#!/bin/bash\nwhile [[ true ]]; do sleep 2; done\n",
  mode    => '0755',  # Make the script executable
}
