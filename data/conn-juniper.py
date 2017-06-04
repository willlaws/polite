#!/usr/bin/python3

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from pprint import pprint
import argparse
from json_to_junos import json_to_junos

def main():
    vmx7 = {
        'host': '54.69.184.104',
        'user': 'ntc',
        'password': 'ntc123',
    }

    parser = argparse.ArgumentParser()
    #parser.add_argument("--config", help="Configuration file")
    parser.add_argument("--json", help="JSON file")
    args = parser.parse_args()
    
    config = json_to_junos(args.json)    

    dev = Device(**vmx7)
    dev.open()
    cfg = Config(dev)
    cfg.load(config, format="text", merge=True)
    cfg.pdiff()

if __name__ == '__main__':
    main()
