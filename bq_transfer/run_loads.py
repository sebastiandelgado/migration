import subprocess
import sys

path = sys.argv[1] # from gs:// to month/; ex: gs://scribefiles-bigquery-4/impression_json/2012/12/
table = sys.argv[2]
year = sys.argv[3]
month = sys.argv[4]
subprocess.call("gsutil ls "+ path + " > rl_temp.txt", shell=True)
subprocess.call("wc -l rl_temp.txt > rl_temp_len.txt", shell=True)

len_tempfile = open("rl_temp_len.txt", "r")
tempfile_length = int(len_tempfile.readline()[:-12])
num_thousands = (tempfile_length / 1000) + 1


tempfile = open("rl_temp.txt", "r")
example = tempfile.readline()

for i in range(num_thousands):
	path_wild = example[:-5] + str(i) + "*"
	log_name =  table + "_" + year + "_" + month + "-" + str(i) + ".txt" 
	print "bq load --source_format=NEWLINE_DELIMITED_JSON --max_bad_records=9900000 test."+table+" "+path_wild+" > load-logs/"+log_name+" &"
	#print path_wild
	#print log_name
