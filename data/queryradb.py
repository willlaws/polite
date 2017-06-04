#!/usr/bin/env python

import subprocess
import re

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
	name = queryname(2381)
	prefixes = queryprefixes(2381,'whois.radb.net')

	print("Name: ", name)
	print("Prefixes: ", prefixes)


if __name__ == "__main__":
	main()

