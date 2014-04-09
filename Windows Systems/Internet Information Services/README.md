Zabbix-IIS-Template
=================

This template use Zabbix agent to discover and monitor Microsoft Internete Information Servers

Items
-----

  *  ASP.Net Application restarts
  *  ASP.Net Errors Total/sec
  *  ASP.Net Number of current requests
  *  ASP.Net Requests/Sec
  
  *  [DISCOVERY] SiteName: Current anonymous users
  *  [DISCOVERY] SiteName: Current connections
  *  [DISCOVERY] SiteName: Current nonanonymous users
  *  [DISCOVERY] SiteName: Get requests/s
  *  [DISCOVERY] SiteName: Head requests/s
  *  [DISCOVERY] SiteName: Post requests/s

Triggers
--------

  *  [MEDIUM] IIS application pool restarted

Graphs
------

  *  IIS ASP.NET Counters overview 

  *  [DISCOVERY] SiteName: Requests
  *  [DISCOVERY] SiteName: Connections

Installation
------------

1. Install the Zabbix agent on your host or download my automated package
2. Install [`WindowsDiscovery.vbs`]()  in the script directory of your Zabbix proxy: `<zabbix_script_path>`  (Don't forget to edit username/passwords)
3. Add the following line to your Zabbix agent configuration file. Note that `<zabbix_script_path>` is your Zabbix proxy script path :

    UnsafeUserParameters=1
    UserParameter = Windows.discovery[*],%systemroot%\system32\cscript.exe /nologo /T:30 "`<zabbix_script_path>`\WindowsDiscovery.vbs" "$1"

4. Edit username and password parameters on getdb.vbs
5. Import [`Zabbix-IIS-Template.xml`]() file into Zabbix.
6. Associate "Template SQLServer" template to the host.


Requirements
------------

This template was tested for Zabbix 2.2.1 and higher.

##### [Zabbix agent](http://www.zabbix.com) 2.0.x
##### [`WindowsDiscovery.vbs`]() 1.0

License
-------

This template is distributed under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the  License, or (at your option) any later version.