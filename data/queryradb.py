#!/usr/bin/env python

import subprocess

command = ['whois', '-h', 'whois.radb.net', '!gas2381']

response = subprocess.check_output(command)
prefixes = response.split("\n")[1].split(" ")

print(prefixes)




