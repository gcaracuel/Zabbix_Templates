"""
Reads a CSV file (Format= <IP>,<Shop/router name>), adds it to the discovery rules and update its visible name if it exist
We prefer this to manually add and remove hosts because of discovery rules auto remove action

Take care there is a limit in 255 chars with IP_RANGE string. This script will use as many drules as neccesary, please create them before with name format "Cisco Router xx". 

"""

from pyzabbix import ZabbixAPI
import csv

import MySQLdb  # Delete qhen Bug with drules get solved

###
### May change these parameters. Maybe row indexation should be changed
###

ZABBIX_SERVER = 'http://'

ZABBIX_USERNAME = ''

ZABBIX_PASSWORD = ''

CSV_FILE = 'test.csv'

###
###
###


zapi = ZabbixAPI(ZABBIX_SERVER)
zapi.login(ZABBIX_USERNAME,ZABBIX_PASSWORD)


def update_drule (drule_name, ip_range):
	drule = zapi.drule.get(filter={"name": drule_name})
	zapi.drule.update(druleid=drule[0]["druleid"], iprange=ip_range)


def update_host_alias (host_name, host_alias):
	hosts = zapi.host.get(filter={"host": host_name})
	if hosts:
		zapi.host.update(hostid=hosts[0]["hostid"],  name=host_alias)


def update_drule_DB (drule_name,ip_range):
	db = MySQLdb.connect(host="localhost", user="root", db="zabbix")
	cur = db.cursor()
	query = "UPDATE drules SET iprange=\'" + ip_range + "\' WHERE name like '"+ drule_name + "';"
	cur.execute(query)
	db.commit()	



IP_RANGE = []
reader = csv.reader(open(CSV_FILE, 'rb'))


###
###	Change row indexation to adjust CSV format
###
for index,row in enumerate(reader):
	IP_RANGE.append(row[0])
	update_host_alias(row[0],row[1])


# Discovery Rules's IP Range has a limitation of 255 chars we'll need to use multiple DRules

chunks=[IP_RANGE[x:x+15] for x in xrange(0, len(IP_RANGE), 15)]




# There is a BUG in Zabbix API with drule.update method, until it is silved we must to update 'iprange' manually in database

# Uncomment when BUG ZBX-6257 get solved

#	

#	for idx, val in enumerate(chunks):
#		IP_RANGE_FIXED = ",".join(val)
#		update_drule_DB("Routers Cisco "+ str(idx+1) ,IP_RANGE_FIXED)	#DRULE name maybe formatted as "Routers Cisco 1", "Routers Cisco 2","Routers Cisco 3", etc.





# Manually update using SQL. Comment this lines when uncomment the previous ones and the function

for idx, val in enumerate(chunks):
	IP_RANGE_FIXED = ",".join(val)
	update_drule_DB("Routers Cisco "+ str(idx+1) ,IP_RANGE_FIXED)
