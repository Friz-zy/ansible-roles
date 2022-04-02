distro types: deb

install: nginx

modify: /etc/nginx/dhparams.pem, /etc/nginx/sites-enabled/default, /etc/pam.d/nginx, www-data group-> shadow, /etc/nginx.conf, /etc/nginx/conf.d

restart:

vars: -
