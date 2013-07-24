import sys
import subprocess

object_file_path = sys.argv[1]
instance_index = sys.argv[2]
num_instances = sys.argv[3]


# Generates the my_objects text file containing all the objects corresponding to this instance
def genMyObjects(instance_i, n_instances):
	all_objects = open(object_file_path, "r")
	my_objects = open("my_objects", "w")
	line = all_objects.readline()
	while line:
		end_num = int(line[len(line)-4:])
		if end_num%n_instances == instance_i:
			my_objects.write(line)
		line = all_objects.readline()
	all_objects.close()
	my_objects.close()

genMyObjects(int(instance_index), int(num_instances))

subprocess.call("cat my_objects | gsutil -m cp -InL manifest_"+str(instance_index)+" gs://scribefiles-bigquery-4/", shell=True)
print "DONE"
subprocess.call("mkdir it_is_done", shell=True)
subprocess.call("gcutil deleteinstance -f mw"+ str(instance_index), shell=True) 









