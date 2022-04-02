distro types: docker-compose

install: vmagent vmauth victoriametrics vmalert

modify: 

restart: systemctl nginx vmagent vmauth victoriametrics vmalert alertmanager grafana

vars:
vm_compose_dir: /opt/victoriametrics
vm_data_dir: /data
vm_site: vmetrics.example.com 
vm_domain: example.com
vm_user_admin: admin
vm_user_admin_pass: ''                             
vm_user_select: select
vm_user_select_pass: ''                             
vm_user_insert: insert 
vm_user_insert_pass: ''