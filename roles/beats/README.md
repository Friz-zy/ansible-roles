distro types: deb, rpm

install: filebeat, metricbeat, packetbeat, heartbeat

modify: configs, systemd services

restart: systemd, nginx, filebeat, metricbeat, packetbeat, heartbeat-elastic

vars:
elk_dns:
  site: elk.example.com
elk_user_agent_password: ''
elk_user_kibanaro_password: ''
