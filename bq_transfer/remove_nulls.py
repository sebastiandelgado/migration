import sys
import re

f = open(sys.argv[1], "r")
o = open("apps.clean", "w")

line = f.readline() 
while line:
	line = re.sub(':null,', ':\"\",', line, 100)
	o.write(line)
	line = f.readline()
o.close()
