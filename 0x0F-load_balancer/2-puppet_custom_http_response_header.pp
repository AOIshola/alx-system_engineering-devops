# Automate the task of creating a custom HTTP header response with puppet

$nginx_config = '/etc/nginx/sites-available/default'

$custom_config = "server {
        listen 80;
        listen [::]:80;

        error_page 404 /custom_404.html;
        location = /custom_404.html {
            internal;
            root /var/www/html;
            index index.html;
            try_files $uri $uri/ /index.html;
        }
        location /redirect_me {
                return 301 /var/www/html/redirect_me.html;
        }
        server_name _;

        location / {
                root /var/www/html;
                index index.html index.htm;
        }
}"

file { $nginx_config:
  ensure  => 'file',
  content => $custom_config,
}

exec { 'add_header':
  command     => "sed -i '/server_name.*;/ {/add_header X-Served-By $hostname;/! s/^/ add_header X-Served-By $hostname;\\n/}' $nginx_config",
  path        => '/usr/bin:/bin:/usr/sbin:',
  refreshonly => true
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Exec['add_header'],
}
