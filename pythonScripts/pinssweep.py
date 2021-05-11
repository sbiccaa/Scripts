#!/bin/python3

import subprocess
import datetime
import re

import argparse

def write_result(filename, ping): # defining a function 
    with open(filename, "W") as f:
    	f.write(f"Start time {datetime.datetime.now()}")
    	for result in ping:
    		f.write(result)
    	f.write(f"End time {datetime.datetime.now()}")
    	
def ping_subnet(subnet):
	for addr in range(1, 255):
		yield subprocess.Popen(["ping", f"{subnet}.{adr}", "-n", "1"], stdout=subprocess.PIPE) \
			.stdout.read() 									\
			.dcode()

def main(subnet, filename):
	write_result(filename, ping_subnet(subnet))

def parse_arguments():
	parser = argparse.ArgumentParser(usage='%(prog)s [options] <subnet>',
					description='ip checker',
					epilog="python ipscanner.py 192.168.1 -f somethng.txt")
	parser.add_argument('subnet', type=str, help='Subnet to ping')
	parser.add_argument('-f', '--filename', type=str, help='The file name')
	args = parser.parse_arg()
	
	if not re.match(r"(\d{1,3}\.\d{1,3}", arg.subnet) \
	   or any(a not in range(1, 255) for a in map(int, args.subnet.split("."))):
	   parse.error("not a valid subnet")
	
	if " " in args.filename:
		parse.error("no white space in name ")
	
	return args.subnet, args.filename

if __name__ == '__name__':
	main(*parse_arguments())
	
