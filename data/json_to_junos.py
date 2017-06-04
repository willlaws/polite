#!/usr/bin/python
from jinja2 import Template
import argparse
import json


def json_to_junos(json_file):
    json_data = open(json_file).read()
    data = json.loads(json_data)
    config = ''
    pref_temp = Template('''
        policy-options prefix-list PEER-{{ name }}-v4-IN {
        {% for prefix in prefixes %}
            {{ prefix }};
        {% endfor %}
        }
        policy-options policy-statement cust_{{ name }} {
            term 1 {
                from {
                    prefix-list PEER-{{ name }}-v4-IN;
                }
                then accept;
            }
            term 2 {
                then reject;
            }
        }

    ''')
    for i in data['asns']:
        name = data['asns'][i]['name']
        prefixes = []
        for n in data['asns'][i]['prefixes']:
            prefixes.append(n)
        # print prefixes
        config = config + pref_temp.render(asn=i, prefixes=prefixes, name=name)
    return config

