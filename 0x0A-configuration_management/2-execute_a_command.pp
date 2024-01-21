# kills a process named killmenow

exec { 'killmenow':
  command   => 'pkill -f killmenow',
  path      => ['/usr/bin', '/usr/sbin', '/bin'],
  provider  => 'shell',
  onlyif    => '/usr/bin/pgrep -f killmenow',
  logoutput => true,
}
