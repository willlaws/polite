#!/usr/bin/env python

import argparse
import json
import re
import subprocess
import time

def queryname(asn, queryhost='whois.radb.net'):
	command = ['whois', '-h', queryhost, 'as{}'.format(asn)]

	response = subprocess.check_output(command)
	lines = response.split("\n")

	nameline = filter(lambda line: re.match("^as-name:", line), lines)[0]

	name = re.search("^as-name:\s+(.*)$", nameline).group(1)
	
	return(name)

def queryprefixes(asn, queryhost='whois.radb.net'):
	command = ['whois', '-h', queryhost, '!gas{}'.format(asn)]

	response = subprocess.check_output(command)
	prefixes = response.split("\n")[1].split(" ")
	
	return(prefixes)

def createas(name, prefixes):
	return { 'name': name, 'prefixes': prefixes }

def createjson(asns):
	data = {}

	data['timestamp'] = time.time()
	data['asns'] = asns

	return json.dumps(data)

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("--asn", nargs='+', type=int, required=True)
	parser.add_argument("--host", default="whois.radb.net")
	args = parser.parse_args()

	asns = {}

	for asn in args.asn:
		name = queryname(asn, args.host)
		prefixes = queryprefixes(asn, args.host)

		asns[asn] = createas(name, prefixes)

	print createjson(asns)

if __name__ == "__main__":
	main()

