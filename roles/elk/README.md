distro types: deb, rpm

install: elasticsearch, logstash, kibana, curator

modify: /etc/hosts, /etc/nginx, /etc/kibana, /etc/apm-server, /etc/logstash, /etc/elasticsearch, /etc/curator

restart: elasticsearch, logstash, kibana, apm, nginx

vars:
es_cluster_name: elasticsearch_production
elk_dns:
  domain: example.com
  site: elk.example.com
elk_apm_secret_token: ''
elk_user_admin_password: ''
elk_user_kibanaserver_password: ''
elk_user_kibanaro_password: ''
elk_user_logstash_password: ''
elk_user_readall_password: ''
elk_user_snapshotrestore_password: ''
elk_user_agent_password: ''
elk_user_apm_password: ''
