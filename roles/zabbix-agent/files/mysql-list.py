#!/usr/bin/env python2

import os
import re
import json

# show slave status; Empty set

def main():
    if os.geteuid() != 0:
        return os.execvp("sudo", ["sudo"] + ["python"] + sys.argv)

    data = {"data": []}
    try:
        with open('/root/.my.cnf', 'r') as f:
            mycnf = f.read()
            instances = re.findall(r'(?<=client).*(?=])', mycnf)
    except:
        instances = ['']
    for i in instances:
        data["data"].append({"{#MYSQLCLIENT}": i})
    print json.dumps(data)

if __name__ == '__main__':
    main()
