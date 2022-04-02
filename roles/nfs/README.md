distro types: deb, rpm

install: nfs-server

modify: /etc/exports

restart: nfs-kernel-server, mount all

vars:
nfs_export: ""
nfs_mount: ""
