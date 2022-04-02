distro types: deb, rpm

install: mysql

modify: 

restart: mysql

vars:
mysql_conf_bind_address: 0.0.0.0 # default is 127.0.0.1
mysql_conf_relay_log_space_limit: 100M
mysql_conf_log_bin: /var/log/mysql/mysql-bin.log
mysql_conf_expire_logs_days: 1
mysql_conf_max_binlog_size: 100M
mysql_conf_wsrep_on: "OFF"
mysql_conf_wsrep_cluster_address: "gcomm://"
mysql_conf_wsrep_cluster_name: galera
mysql_monitoring_user: monitoring
mysql_monitoring_pass: monitoring
mysql_monitoring_grants: "mysql.*:SELECT/*.*:SHOW DATABASES"

