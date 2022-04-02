#!/usr/bin/env python

import sys
import pyzabbix
import yaml
import argparse


TCHECK = {
    "delay": "60",
    "status": "0",
    "agent": "Zabbix",
    "retries": "2",
    "steps": []
    }

TSTEP = {
    "no": "1",
    "timeout": "30",
    "status_codes": "200",
    "follow_redirects": "1",
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', default="http://localhost/zabbix", help='Zabbix server url')
    parser.add_argument('-u', help='Zabbix user')
    parser.add_argument('-p', help='Zabbix password')
    parser.add_argument('-c', default="./webchecks.yml", help='Configuration yaml file path')
    args, unknown = parser.parse_known_args()

    with open(args.c, 'r') as stream:
        checks = yaml.load(stream)

    zapi = pyzabbix.ZabbixAPI(args.s)
    zapi.login(args.u, args.p)

    hosts = {}
    for h in zapi.host.get(output="extend"):
        hosts[h["host"]] = h['hostid']

    echecks = {}
    for c in zapi.httptest.get(output="extend"):
        echecks[c["name"]] = {
            'httptestid': c['httptestid'],
            'hostid': c['hostid']
            }


    triggers = {}
    for t in zapi.trigger.get(output="extend"):
        triggers[t['description']] = t['triggerid']
#>>> zapi.trigger.get(output="extend")[0]
#{u'status': u'1', u'recovery_mode': u'0', u'description': u'Processor load is too high on {HOST.NAME}', u'state': u'0', u'url': u'', u'type': u'0', u'templateid': u'0', u'correlation_tag': u'', u'lastchange': u'0', u'value': u'0', u'priority': u'2', u'triggerid': u'10010', u'flags': u'0', u'comments': u'', u'error': u'', u'correlation_mode': u'0', u'expression': u'{15606}>5', u'recovery_expression': u'', u'manual_close': u'0'}


    exceptions = []
    for check in checks:
        try:
            echeck = echecks.get(check['name'], None)
            hostid = hosts.get(check['host'])
            c = dict(TCHECK)
            c.update(check)
            c['steps'] = []
            for i, step in enumerate(check['steps']):
                s = dict(TSTEP)
                s.update(step)
                s['no'] = i + 1
                c['steps'].append(s)
            c['hostid'] = hostid

            # zapi.httptest.update can't change hostid
            # so we should delete and create it again

            # TODO: https://serverfault.com/questions/634987/zabbix-send-a-very-large-of-false-alarms
            if echeck:
                checkid = echeck['httptestid']
                if hostid != echeck['hostid']:
                    zapi.httptest.delete(checkid)
                    print("Old check '%s' deleted") % (c['name'].encode('utf-8'))
                    echeck = None
                    tname = 'Web scenario "%s" failed' % (c['name'].encode('utf-8'))
                    if tname in triggers:
                        zapi.trigger.delete(triggers[tname])
                        print("Old trigger \"%s\" deleted") % (tname)

            if echeck:
                del c['hostid']
                del c['host']
                c['httptestid'] = echeck['httptestid']
                zapi.httptest.update(c)
                print("Check '%s' updated") % (c['name'].encode('utf-8'))
            else:
                del c['host']
                zapi.httptest.create(c)
                print("Check '%s' created") % (c['name'].encode('utf-8'))
                tname = 'Web scenario "%s" failed' % (c['name'].encode('utf-8'))
                zapi.trigger.create({
                    "description": tname,
                    "priority": 4,
                    "manual_close": 1,
                    "expression": '{%s:web.test.error[%s].strlen()}>0 ' % (check['host'], c['name']) + \
                        'and {%s:web.test.fail[%s].last()}>0'  % (check['host'], c['name']),
                    })
                print("New trigger \"%s\" created") % (tname)
        except Exception as e:
            exceptions.append((check['name'], e))

    if exceptions:
        for e in exceptions:
            print("Adding '%s' failed: %s") % (e[0].encode('utf-8'), e[1])
        sys.exit(1)

if __name__ == '__main__':
    main()
