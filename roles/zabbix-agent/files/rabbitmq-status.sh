#!/bin/bash
#UserParameter=rabbitmq[*],<%= zabbix_script_dir %>/rabbitmq-status.sh

# add random sleep
sleep $((RANDOM % 10))

NODE=$(echo $1| sed 's!__dog__!@!g')
VHOST=$2
METRIC=$3
ITEM=$4

CMD="sudo /usr/sbin/rabbitmqctl -n $NODE -p $VHOST"
NAME="$NODE-$VHOST-$METRIC"
NAME1="${NAME//\//\\}"
CACHE="/tmp/rabbitmq-$NAME1"
if [ -e $CACHE ]; then
    LAST_MODIFY=$(($(date +%s) - $(date +%s -r $CACHE)))
else
    LAST_MODIFY="1000"
fi

#rabbitmq[rabbit,\/,list_queues,none]
if [ "$METRIC" = "list_queues" ]; then
    if [ "$LAST_MODIFY" -gt "60" ]; then
        $CMD list_queues > $CACHE
    fi
    cat $CACHE | grep -cv '\.\.\.'
fi

#rabbitmq[rabbit,\/,list_exchanges,none]
if [ "$METRIC" = "list_exchanges" ]; then
    if [ "$LAST_MODIFY" -gt "60" ]; then
        $CMD list_exchanges > $CACHE
    fi
    cat $CACHE | grep -cv '\.\.\.'
fi

#rabbitmq[rabbit,\/,queue_durable,queue-name]
if [ "$METRIC" = "queue_durable" ]; then
    if [ "$LAST_MODIFY" -gt "60" ]; then
        $CMD list_queues name durable > $CACHE
    fi
    cat $CACHE | grep "^$ITEM\s.*$" | awk '{ print $2 }'
fi

#rabbitmq[rabbit,\/,queue_msg_ready,queue-name]
if [ "$METRIC" = "queue_msg_ready" ]; then
    if [ "$LAST_MODIFY" -gt "60" ]; then
        $CMD list_queues name messages_ready > $CACHE
    fi
    cat $CACHE | grep "^$ITEM\s.*$" | awk '{ print $2 }'
fi

#rabbitmq[rabbit,\/,queue_msg_unackd,queue-name]
if [ "$METRIC" = "queue_msg_unackd" ]; then
    if [ "$LAST_MODIFY" -gt "60" ]; then
        $CMD list_queues name messages_unacknowledged > $CACHE
    fi
    cat $CACHE | grep "^$ITEM\s.*$" | awk '{ print $2 }'
fi

#rabbitmq[rabbit,\/,queue_msgs,queue-name]
if [ "$METRIC" = "queue_msgs" ]; then
    if [ "$LAST_MODIFY" -gt "60" ]; then
        $CMD list_queues name messages > $CACHE
    fi
    cat $CACHE | grep "^$ITEM\s.*$" | awk '{ print $2 }'
fi

#rabbitmq[rabbit,\/,queue_consumers,queue-name]
if [ "$METRIC" = "queue_consumers" ]; then
    if [ "$LAST_MODIFY" -gt "60" ]; then
        $CMD list_queues name consumers > $CACHE
    fi
    cat $CACHE | grep "^$ITEM\s.*$" | awk '{ print $2 }'
fi

#rabbitmq[rabbit,\/,queue_memory,queue-name]
if [ "$METRIC" = "queue_memory" ]; then
    if [ "$LAST_MODIFY" -gt "60" ]; then
        $CMD list_queues name memory > $CACHE
    fi
    cat $CACHE | grep "^$ITEM\s.*$" | awk '{ print $2 }'
fi

#rabbitmq[rabbit,\/,exchange_durable,exchange-name]
if [ "$METRIC" = "exchange_durable" ]; then
    if [ "$LAST_MODIFY" -gt "60" ]; then
        $CMD list_exchanges name durable > $CACHE
    fi
    cat $CACHE | grep "^$ITEM\s.*$" | awk '{ print $2 }'
fi

#rabbitmq[rabbit,\/,exchange_type,exchange-name]
if [ "$METRIC" = "exchange_type" ]; then
    if [ "$LAST_MODIFY" -gt "60" ]; then
        $CMD list_exchanges name type > $CACHE
    fi
    cat $CACHE | grep "^$ITEM\s.*$" | awk '{ print $2 }'
fi

