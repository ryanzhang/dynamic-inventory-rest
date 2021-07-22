#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import json
import os
import socket
import subprocess


def main():
    print(json.dumps(inventory(), sort_keys=True, indent=2))


def inventory():
    # ip_address = find_pi()
    ip_address = "192.168.2.15"

    for k, v in sorted(os.environ.items()):
        print(k+':', v)
    print('\n')

    return {
        'all': {
            'hosts': [ip_address],
            'vars': {},
        },
        '_meta': {
            'hostvars': {
                ip_address: {
                    'ansible_ssh_user': 'root',
                }
            },
        },
        'pi': [ip_address]
    }


def find_pi():
    for ip in all_local_ips():
        if port_22_is_open(ip):
            return ip


def all_local_ips():
    lines = subprocess.check_output(['arp', '-a']).split('\n')
    for line in lines:
        if '(' not in line:
            continue
        after_open_bracket = line.split('(')[1]
        ip = after_open_bracket.split(')')[0]
        yield ip


def port_22_is_open(ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip, 22))
    return result == 0


if __name__ == '__main__':
    main()
