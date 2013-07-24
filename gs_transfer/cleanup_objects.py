import re
import sys

path = sys.argv[1]
new_name = sys.argv[2]

origin_file = open(path, "r")
need = open(new_name, "w")

# nothing that ends in a dollar sign or in a /:

current_line = origin_file.readline()

while current_line:
	if re.search(r'\$', current_line) or re.search(r':$', current_line):
		pass
	elif current_line.strip():
		need.write(current_line)
	current_line = origin_file.readline()

origin_file.close()
need.close()
