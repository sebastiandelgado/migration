import sys
import subprocess

directory = sys.argv[1]
tables = ["impression", "impressions_miss", "transaction", "bootup", "install", "click"]

for table in tables:
	subprocess.call("gsutil ls -R gs://scribefiles-bigquery/"+table+"_json/ > "+directory+"/"+table+"_objects_dirty" , shell=True)
	subprocess.call("python gen_all_files.py "+directory+"/"+table+"_objects_dirty "+directory+"/"+table+"_objects", shell=True)
	