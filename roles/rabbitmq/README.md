distro types: rpm, deb

install: rabbitmq-server

modify: 

restart: rabbitmq-server

vars:
rabbitmq_user: user
rabbitmq_password: ""


https://www.rabbitmq.com/install-rpm.html
https://packagecloud.io/rabbitmq/rabbitmq-server
https://www.rabbitmq.com/memory.html
https://www.rabbitmq.com/management.html

To use the web UI you will need to authenticate as a RabbitMQ user (on a fresh installation the user "guest" is created with password "guest"). From here you can manage exchanges, queues, bindings, virtual hosts, users and permissions. Hopefully the UI is fairly self-explanatory.

https://www.rabbitmq.com/access-control.html
https://www.rabbitmq.com/rabbitmqctl.8.html#User_Management
https://gist.github.com/sdieunidou/1813409ddfd0185c82c7
