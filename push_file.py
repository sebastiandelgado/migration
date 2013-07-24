import subprocess
import sys

num_instances = sys.argv[1]
file_path = sys.argv[2]

for i in range (int(num_instances)):
	subprocess.call("nohup gcutil push mw"+str(i)+" "+file_path+" "+file_path+" &", shell=True)