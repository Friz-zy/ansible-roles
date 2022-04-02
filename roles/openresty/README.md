distro types: deb

install: openresty, luarocks

modify: /etc/openresty, /var/log/openresty, /etc/openresty/nginx.conf, /etc/logrotate.d/openresty

restart: openresty

vars:  
openresty_config_path: /usr/local/openresty/nginx/conf  
openresty_sites_path: /etc/openresty/sites-enabled  

