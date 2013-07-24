import subprocess
import sys

num_instances = sys.argv[1]
#prefix = sys.argv[2]

print "deleting INSTANCES"
for i in range (int(num_instances)):
	#if i < 10: i = "0"+str(i)
	subprocess.call("nohup gcutil deleteinstance -f mw"+str(i)+" &", shell=True)