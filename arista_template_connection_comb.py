#!/usr/bin/env python

import pyeapi
import jinja2
import json
from pprint import pprint as pp

template = '''
{%- for p_list in data['prefixes'] -%}
ip prefix-list {{ data.name }} seq {{ seq_num }} permit {{ p_list }}
{% set seq_num = seq_num + 1 -%}
{% endfor -%}
'''


def arista_connect(configs):

    node = pyeapi.connect_to('eos-spine1')
    node.config(configs)
    #node = pyeapi.connect(transport='https', host='52.42.142.250', username='ntc', password='ntc123', timeout=120)
    #node.execute(configs)

def create_template():

    conf_list = []

    with open("huge_file.json") as json_data:
        info = json.load(json_data)

    t = jinja2.Template(template)
    asn_list = info['asns'].keys()

    for i in asn_list:
        abcd = info['asns'][i]
        out = t.render(data=abcd, seq_num=1)
        conf_list += ([y for y in (x.strip() for x in out.splitlines()) if y])

    return conf_list

def main():

    arista_connect(create_template())

if __name__ == "__main__":
    main()