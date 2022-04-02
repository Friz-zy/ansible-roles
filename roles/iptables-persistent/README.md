distro types: deb

install: iptables-persistent

modify: /lib/systemd/system/netfilter-persistent.service

restart: netfilter-persistent, systemctl

vars: -
