#!/usr/local/bin/python2.7
import boto.ec2
import key
import boto

conn = boto.ec2.connect_to_region("us-west-1",aws_access_key_id=key.acc_tok,aws_secret_access_key=key.acc_sec)
reservations = conn.get_all_instances()
print reservations
for i in reservations:
	for j in i.instances:
		print j.ip_address, j.vpc_id, j.state, j.instance_type, j.private_ip_address


##we can do dir(j) for looking up the methods avaiable
conn1 = boto.connect_iam(aws_access_key_id=key.acc_tok,aws_secret_access_key=key.acc_sec)
d = conn1.get_all_users()
for i in range(0,len(d['list_users_response']['list_users_result']['users'])):
	print d['list_users_response']['list_users_result']['users'][i]['user_name']
