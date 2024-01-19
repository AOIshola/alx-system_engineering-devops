# installs flask version 2.1.0

package { 'werkzeug':
  ensure   => 'latest',
  provider => 'pip3',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['werkzeug'],
}
