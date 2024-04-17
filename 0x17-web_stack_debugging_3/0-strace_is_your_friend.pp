file {'/var/www/html/wp-settings.php':
    ensure => file,
}

replace { 'wp-setting-php-typo':
    target   => '/var/www/html/wp-settings.php',
    regexp   => 'phpp',
    replace  => 'php',
    before   => File[''/var/www/html/wp-settings.php'],
    provider => 'posix',
}

notify { 'Reload Apache':
  exec => 'sudo /usr/sbin/service apache2 reload',
}
