import re
import sys

path = sys.argv[1]

origin_file = open(path, "r")
ips = open("ext_ip.txt", "w")

current_line = origin_file.readline()

while current_line:
	if re.search(r'173\..*', current_line):
		ips.write("\"")
		ips.write(re.search(r' 173\..* ', current_line).group(0)[1:16])
		ips.write("\", ")
	current_line = origin_file.readline()

