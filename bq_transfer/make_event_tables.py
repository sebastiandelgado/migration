
import sys
import subprocess
# Arguments: projectID and dataset name (they must both be previously created)

dataset = sys.argv[1]


tables = ["transaction", "impression", "click", "install", "bootup", "impressions_miss", "apps", "campaigns"]

for table in tables:
	subprocess.call("bq rm -tf "+dataset+"."+table, shell=True)
	subprocess.call("bq mk -t "+dataset+"."+table+" bq_schemas_2/"+table+"_schema.txt", shell=True)


	