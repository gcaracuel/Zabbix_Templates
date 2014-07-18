jetNexus-LoadBalancer-Template
=================

This template use Zabbix agent to monitor jetNexus load balancers.
Maybe this will need to be adapted for your desired interval checking and show value mappings, applications, etc.

Items
-----

  *  CPU Usage
  *  Total Bytes IN Delta
  *  Total Bytes OUT Delta
  *  Uptime

  *  Total Connections
  *  Total Current Connections
  *  Total IDLE Connections
  *  Total SSL Connections
  *  Total Requests

  *  [DISCOVERY: Interface] Interface RXBytes Delta
  *  [DISCOVERY: Interface] Interface TXBytes Delta

  *  [DISCOVERY: Node] Current Connections
  *  [DISCOVERY: Node] Total Connections
  *  [DISCOVERY: Node] State

  *  [DISCOVERY: Pool] IN-Bytes Delta
  *  [DISCOVERY: Pool] OUT-Bytes Delta
  *  [DISCOVERY: Pool] Total Connections
  *  [DISCOVERY: Pool] State

  *  [DISCOVERY: Virtual Service] IN-Bytes Delta
  *  [DISCOVERY: Virtual Service] OUT-Bytes Delta
  *  [DISCOVERY: Virtual Service] Current Connections
  *  [DISCOVERY: Virtual Service] HTTP Cache Hit-rate
  *  [DISCOVERY: Virtual Service] Total Connections

 
Triggers
--------

  *  [Disaster] CPU Usage = 100% (DISABLED)
  *  [High] CPU Usage > 90%
  *  [Average] CPU Usage > 80%
  *  [Average] Load balancer seems te has been restarted 
 
  *  [DISCOVERY: Node] [Warning] Node state es not OK
  *  [DISCOVERY: Pool] [Average] Pool state es not OK


Graphs
------

  *  Traffic trend and connections
 
  *  [DISCOVERY: Interface] Interface traffic vs total
  *  [DISCOVERY: Pool] Pool traffic vs total
  *  [DISCOVERY: Virtual Service] VS traffic trend vs total


Scripts
-------

None, all items use SNMP. Please ensure you have configured SNMP client access and community on your load balancers.


License
-------

This template is distributed under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the  License, or (at your option) any later version.