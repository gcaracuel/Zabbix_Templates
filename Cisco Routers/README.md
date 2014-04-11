Cisco-Routers-Template
=================

This template use Zabbix agent to monitor Cisco routers.
Maybe this will need to be adapter your wiring and interface identification.


Items
-----

  *  CPU Usage
  *  ICMP ping
  *  Router name
  *  Temperature
  *  Uptime
  *  Running config last change

  *  Internal Interface (fa0/0) In-bytes
  *  External Interface (fa0/1) In-bytes
  *  Internal Interface (fa0/0) Out-bytes
  *  External Interface (fa0/1) Out-bytes

  *  VPN tunnel active time in seconds
  *  VPN tunnel In-bytes
  *  VPN tunnel Out-bytes
  *  VPN tunnel status

 
Triggers
--------

  *  [Medium] CPU usage is higher than 70%
  *  [Average] CPU usage is higher than 80%
  *  [High] CPU usage is higher than 90%
  *  [Disaster] CPU isage is 100%

  *  [High] Router name changed
  *  [High] Router configuration changed
  *  [Warning] Router restarted

  *  [Average] ICMP ping latency is high
  *  [High] ICMP ping latency is too high
  
  *  [Warning] Temperature higher than 50ºC
  *  [Medium] Temperature higher than 65ºC
  *  [High] Temperature higher than 70ºC


Graphs
------

  *  Interfaces traffic
  *  Temperature
  *  VPN tunnel traffic


License
-------

This template is distributed under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the  License, or (at your option) any later version.