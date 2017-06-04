#!/usr/bin/env python

import subprocess

def queryradb(asn, queryhost='whois.radb.net'):
	command = ['whois', '-h', queryhost, '!gas{}'.format(asn)]

	print command
	
	response = subprocess.check_output(command)
	prefixes = response.split("\n")[1].split(" ")
	
	return(prefixes)

def main():
	print(queryradb(2381,'whois.radb.net'))


if __name__ == "__main__":
	main()

