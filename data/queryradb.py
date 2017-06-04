#!/usr/bin/env python

import subprocess
import re
import argparse

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

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("--asn", type=int, required=True)
	parser.add_argument("--host", default="whois.radb.net")
	args = parser.parse_args()


	name = queryname(args.asn, args.host)
	prefixes = queryprefixes(args.asn, args.host)

	print("Name: ", name)
	print("Prefixes: ", prefixes)


if __name__ == "__main__":
	main()

