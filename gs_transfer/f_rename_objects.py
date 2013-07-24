import subprocess
import os
import mmap
import re
import time
import sys

flat_names_file = sys.argv[1]
nested_names_file = sys.argv[2] # must have s3:// prefix
s3_prefix = sys.argv[3] # format: s3://bucket_name/
gs_prefix = sys.argv[4] # format: gs://bucket_name/
s3_prefix_len = len(s3_prefix)

size = os.stat(nested_names_file).st_size
all_files = open(nested_names_file, "r")
data = mmap.mmap(all_files.fileno(), size, access=mmap.ACCESS_READ)
old_file_names = open(flat_names_file, "r")

old_name = old_file_names.readline()
while old_name: 
	old_name = old_name[:-1]
	new_name = gs_prefix + re.search(s3_prefix+r'.*'+old_name[s3_prefix_len:], data).group(0)[s3_prefix_len:]
	print "old object name: " + old_name
	print "new object name: " + new_name
	subprocess.call("nohup gsutil mv " + old_name + " " + new_name + " &", shell=True)
	old_name = old_file_names.readline()



# MAKE SURE I GOT CLEAN LOAD
# CHANGE NAMES TO NESTED FORMAT
# START LOAD JOBS INTO BIGQUERY

# There should be 92872
# 92371 objects at 7am
# 
