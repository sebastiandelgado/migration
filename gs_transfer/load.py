import sys
import subprocess
import re
import time

# Needs to be in the same directory as the file

table_year_month = sys.argv[1]
instance_index = sys.argv[2]
total_instances = sys.argv[3]

all_objects = open("all_files", "r")
my_objects = open("my_objects", "w")


line = all_objects.readline()
while line:
	if re.search(table_year_month, line) and int(line[len(line)-3:])%int(total_instances) == 0:
		my_objects.write(line)
	line = all_objects.readline()

t = str(time.time())

subprocess.call("cat my_objects | gsutil -m cp -InL manifest_"+ t +" gs://cb_bigquery/"+table_year_month, shell=True)

subprocess.call("gsutil -m cp manifest_"+t+" gs://manifests", shell=True)
