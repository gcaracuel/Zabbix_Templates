Cisco-Routers-Template
=================

This template use Zabbix agent to monitor Cisco routers.


Items
-----

  *  CPU Usage
  *  ICMP latency
  *  Router name
  *  Temperature
  *  Uptime in secs
  *  Running config last change

  *  VPN tunnel Uptime
  *  VPN tunnel IN-Bytes
  *  VPN tunnel OUT-Bytes
  *  VPN tunnel Status

  *  [DISCOVERY] Interface IN-Bytes Delta
  *  [DISCOVERY] Interface OUT-Bytes Delta

 
Triggers
--------

  *  [Warning] CPU usage is higher than 80%
  *  [Average] CPU usage is higher than 90%
  *  [High] CPU isage is 100%

  *  [High] Router name changed
  *  [High] Router configuration changed
  *  [Warning] Router restarted

  *  [Average] ICMP ping latency is high
  *  [High] ICMP ping latency is too high
  
  *  [Warning] Temperature higher than 50ºC
  *  [Medium] Temperature higher than 65ºC
  *  [High] Temperature higher than 70ºC

  *  [Average] VPN tunnel is DOWN


Graphs
------

  *  CPU Usage vs router temp
  *  Latency
  *  VPN tunnel traffic

  *  [DISCOVERY] Interface traffic


Scripts
-------

['SNMP_Tunnel_Check.py']() and ['SNMP_Tunnel_Check.sh']() will be executed as a Zabbix external script, please check Zabbix documentation to make it work.
This script will answer 4 metrics: [IN-Bytes, OUT-Bytes, Status, Uptime] all them sumarized for all split tunnels in the VPn connection.

EXTRA: [`RouterDiscoveryZabbix.py`]() A basic script to configure an existent discovery rule with a list (given a CSV) of your router. It will allow you to name your router using 'Visible Name'. Use it in a big firt import or if your big router list will change frecuently.


License
-------

This template is distributed under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the  License, or (at your option) any later version.