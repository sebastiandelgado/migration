import subprocess
import os
import mmap
import re
import time
import sys

flat_names_file = sys.argv[1]
nested_names_file = sys.argv[2] # must have s3:// prefix

size = os.stat(nested_names_file).st_size
all_files = open(nested_names_file, "r")
data = mmap.mmap(all_files.fileno(), size, access=mmap.ACCESS_READ)
old_file_names = open(flat_names_file, "r")

old_name = old_file_names.readline()
while old_name: 
	old_name = old_name[:-1]
	new_name = "gs://cb-bigquery" + re.search(r's3://scribefiles-bigquery/.*'+old_name[26:], data).group(0)[25:]
	print "old object name: " + old_name
	print "new object name: " + new_name
	subprocess.call("gsutil mv " + old_name + " " + new_name, shell=True)
	old_name = old_file_names.readline()

print "DONE!"