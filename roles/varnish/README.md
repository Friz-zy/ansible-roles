distro types: deb

install: varnish

modify: /lib/systemd/system/varnish.service, /etc/default/varnish, /etc/sysconfig/varnish, /etc/varnish/varnish.params

restart: varnish

vars:  
varnish_storage_backend_option: 'malloc,256m'  
varnish_ttl_option: 120  
