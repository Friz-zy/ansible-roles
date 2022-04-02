#!/usr/bin/env python2

import os
import sys
import ssl
import yaml
import json
import OpenSSL
import argparse
from datetime import datetime


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('domain', nargs='?',
                        help='Domain for checking')
    parser.add_argument('--list', action='store_true',
                        default=False, help='Return list of domains in zabbix item format')
    parser.add_argument('-c', default=os.path.dirname(os.path.realpath(__file__)) + "/sslchecks.yml",
                        help='Configuration yaml file path')
    args, unknown = parser.parse_known_args()

    if args.list:
        with open(args.c, 'r') as stream:
            domains = yaml.load(stream)
        data = {"data": []}
        for domain in domains:
            data["data"].append({"{#DOMAIN}": domain})
        print json.dumps(data)
    elif args.domain:
        conn = ssl.create_connection((args.domain, 443))
        context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        sock = context.wrap_socket(conn, server_hostname=args.domain)
        cert = ssl.DER_cert_to_PEM_cert(sock.getpeercert(True))
        x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
        endtime = datetime.strptime(x509.get_notAfter(),"%Y%m%d%H%M%SZ")
        delta = endtime - datetime.now()
        print delta.days

if __name__ == '__main__':
    main()
