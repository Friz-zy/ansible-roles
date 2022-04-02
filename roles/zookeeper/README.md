distro types: deb, rpm

install: zookeeper

modify: /etc/zookeeper/conf/zoo.cfg, /etc/zookeeper/conf/myid

restart: zookeeper

vars:

zookeeper_hosts:
  - {{ inventory_hostname }}
zookeeper_ip: {{ ansible_default_ipv4.address }}