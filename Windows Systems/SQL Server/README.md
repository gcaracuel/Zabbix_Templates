Zabbix-SQLServer-Template
=================

This template use Zabbix agent to discover and manage MS SQL server performance indicators and service status triggers.

BASED ON: [`jjmartress ZBX-WINDOWS-MSSQL template`](https://github.com/jjmartres/Zabbix/tree/master/zbx-templates/zbx-windows/zbx-windows-mssql)

Items
-----

  *  SQL Service State:  Analysis Services
  *  SQL Service State: Integration Services 
  *  SQL Service State: Reporting Services
  *  SQL Service State: SQL Agent [Disabled]
  *  SQL Service State: SQL Browser
  *  SQL Service State: SQL Server
  *  SQL Server: % Buffer cache hit ratio
  *  SQL Server: % Processor Time
  *  SQL Server: Batch Requests per second
  *  SQL Server: Connection memory
  *  SQL Server: Database Pages
  *  SQL Server: Data File Size (Total)
  *  SQL Server: Errors per second
  *  SQL Server: Granted workspace memory
  *  SQL Server: Lock Average Wait Time
  *  SQL Server: Lock blocks
  *  SQL Server: Lock memory
  *  SQL Server: Lock owner blocks
  *  SQL Server: Maximum workspace memory
  *  SQL Server: Memory grants outstanding
  *  SQL Server: Memory grants pending
  *  SQL Server: Optimizer memory
  *  SQL Server: Page life expectancy
  *  SQL Server: Processes Blocked
  *  SQL Server: SQL cache memory
  *  SQL Server: Target server memory
  *  SQl Server: Total server memory

  *  [DISCOVERY] Data file size for each database
  *  [DISCOVERY] Log cache reads per second for each database
  *  [DISCOVERY] Log file size for each database
  *  [DISCOVERY] Log file used size for each database
  *  [DISCOVERY] Percent of log used for each database
  *  [DISCOVERY] Number of transactions per seconds for each database

Triggers
--------

  *  [HIGH] SQL Service State: Analysis Services
  *  [HIGH] SQL Service State: Integration Services 
  *  [HIGH] SQL Service State: Reporting Services
  *  [HIGH] SQL Service State: SQL Agent [Disabled]
  *  [HIGH] SQL Service State: SQL Browser
  *  [HIGH] SQL Service State: SQL Server

Graphs
------

  *  SQL Server Memory Usage

  *  [DISCOVERY] Cache performance per database
  *  [DISCOVERY] Database transaction per second
  *  [DISCOVERY] Disk usage graph for each database

Installation
------------

1. Install the Zabbix agent on your host or download my automated package
2. Install [`WindowsDiscovery.vbs`](https://github.com/gcaracuel/Zabbix_Templates/blob/master/Windows%20Systems/WindowsDiscovery.vbs)  in the script directory of your Zabbix proxy: `<zabbix_script_path>`  (Don't forget to edit username/passwords)
3. Add the following line to your Zabbix agent configuration file. Note that `<zabbix_script_path>` is your Zabbix proxy script path :

    UnsafeUserParameters=1
    UserParameter = Windows.discovery[*],%systemroot%\system32\cscript.exe /nologo /T:30 "`<zabbix_script_path>`\WindowsDiscovery.vbs" "$1"

4. Edit username and password parameters on getdb.vbs
5. Import [`Zabbix-SQLServer-Template.xml`](https://github.com/gcaracuel/Zabbix_Templates/blob/master/Windows%20Systems/SQL%20Server/Zabbix-SQLServer-Template.xml) file into Zabbix.
6. Associate "Template SQLServer" template to the host.


Requirements
------------

This template was tested for Zabbix 2.2.1 and higher.

##### [Zabbix agent](http://www.zabbix.com) 2.0.x
##### [`WindowsDiscovery.vbs`](https://github.com/gcaracuel/Zabbix_Templates/blob/master/Windows%20Systems/WindowsDiscovery.vbs) 1.0

License
-------

This template is distributed under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the  License, or (at your option) any later version.
