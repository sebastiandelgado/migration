import subprocess
import sys

ext_ips = ["173.255.117.105", "173.255.117.104", "173.255.117.250", "173.255.117.223", "173.255.117.243", "173.255.113.79 ", "173.255.117.128", "173.255.117.244", "173.255.117.135", "173.255.117.81 ", "173.255.117.248", "173.255.117.195", "173.255.117.163", "173.255.117.153", "173.255.116.151", "173.255.117.159", "173.255.117.200", "173.255.117.115", "173.255.117.218", "173.255.117.190", "173.255.117.219", "173.255.117.45 ", "173.255.117.192", "173.255.117.102", "173.255.117.90 ", "173.255.117.207", "173.255.117.197", "173.255.117.98 ", "173.255.117.127", "173.255.117.122", "173.255.117.87 ", "173.255.117.165", "173.255.115.199", "173.255.117.126", "173.255.117.220", "173.255.117.17 ", "173.255.117.62 ", "173.255.117.114", "173.255.117.203", "173.255.117.131"]

for i in range(len(ext_ips)):
	print "pushing to mw"+str(i)
	subprocess.call("nohup ssh -o UserKnownHostsFile=/dev/null -o CheckHostIP=no -o  StrictHostKeyChecking=no -i ~/.ssh/google_compute_engine -o LogLevel=QUIET -A  -p 22 chartboost@"+ext_ips[i]+" \"nohup python migrate.py jun24_clean "+str(i)+" 20 &\" &", shell=True)


"""
ssh -o UserKnownHostsFile=/dev/null -o CheckHostIP=no -o  StrictHostKeyChecking=no \
 -i ~/.ssh/google_compute_engine -o LogLevel=QUIET -A  -p 22 chartboost@173.255.113.79 \
 "mkdir it_worked" 

"""
