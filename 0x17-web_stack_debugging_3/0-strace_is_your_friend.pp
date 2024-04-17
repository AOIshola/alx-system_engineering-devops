# fix the webstack of Wordpress site server

$file='/var/www/html/wp-settings.php'
$command='sed -i "s/phpp/php/"'

exec { 'replace-phpp-with-php':
    command => "${command} ${file}",
    path    => ['/bin', '/usr/bin'],
    onlyif  => 'find ${file}',
}

#exec { 'Reload Apache':
  #command => 'sudo service apache reload',
 # path    => ['/bin', '/usr/bin'],
#}
