distro types: deb

install: letsencrypt

modify: nginx configs, cron

restart: nginx

vars:  
letsencrypt_nginx_path: /etc/nginx/sites-enabled
letsencrypt_path: "/var/www/letsencrypt"
letsencrypt_email: "me@example.com"
letsencrypt_sites: []
letsencrypt_nginx_binary: nginx
