import subprocess

n = open("file_names", "r")

for f in n:
	subprocess.call("python make_json.py " + f, shell=True)


