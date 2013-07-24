import subprocess


bucket = "scribefiles-bigquery-3"
tables = ["transaction", "impression", "click", "install", "bootup", "impressions_miss", "apps", "campaigns"]

for t in tables:
	for y in ["2012", "2013"]:
		for i in range(12):
			m = str(i+1)
			if i+1 < 10: m = "0"+str(i+1) 
			subprocess.call("gsutil rm -R gs://" + bucket + "/" + t + "_json/" + y + "/" + m + "/* &", shell=True)
