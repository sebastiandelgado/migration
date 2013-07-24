import subprocess
import sys

num_instances = sys.argv[1]

print "CREATING INSTANCES"
for i in range (int(num_instances)):
	print "CREATING mw"+str(i)
	subprocess.call("nohup gcutil addinstance --image=mw-img-5 --zone=us-central1-a --machine_type=n1-highcpu-4 mw"+str(i)+" &", shell=True)

# ssh -i ~/.ssh/google_compute_engine.pub 173.255.115.15 nohup python migrate.py 00 20 &

# Then:
#	gcutil ssh mwX
#	nohup python migrate.py 00 20 &


# python create_instances.py 40
# python push_file.py 40 jun24_clean
# python push_file.py 40 migrate.py
# python run_instances.py 