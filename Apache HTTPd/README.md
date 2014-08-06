Apache HTTP Server Template
=================

This template uses a daemon to cache Apache mod_status values that will be then queried by a Zabbix script.
Daemon will minimice monitorization resquests to the server caching results. 
Cache daemon should be used as a cron task per objecy server.

Items
-----

  * Total Accesses
  * Total kBytes
  * CPU Load
  * Requests Per Second
  * Bytes Per Second
  * Bytes Per Request
  * Number of Busy Workers
  * Number of Idle Workers

  * Number of slots: Waiting for Connection 
  * Number of slots: Starting up 
  * Number of slots: Reading Request
  * Number of slots: Sending Reply
  * Number of slots: Keepalive (read)
  * Number of slots: DNS Lookup
  * Number of slots: Closing connection 
  * Number of slots: Logging 
  * Number of slots: Gracefully finishing
  * Number of slots: Idle cleanup of worker 
  * Number of slots: Open slot with no current process
  
Triggers
--------

  #### Recomend to create your how trigger to take care of "Waiting for Connection" slot number. Match it to your "MinSpareServer" from "<IfModule prefork.c>
" directive in httpd.conf

Graphs
------

  *  Workers Status
  *  Requests stats (Requests per second and Bytes per request)
  *  Accesses stats (Total accesses and Request per second)

Scripts
-------

['fetch_apachestat.py']() is a Python script that should act a cron task to download regularly mod_status values from server indicated and store it in a cache file. 

['query_apachestat.py']() will be executed as a Zabbix external script. Available metrics (any other will fail):

    # Standard Key:
    # "Total Accesses"
    # "Total kBytes"
    # "CPULoad"
    # "ReqPerSec"
    # "BytesPerSec"
    # "BytesPerReq"
    # "BusyWorkers"
    # "IdleWorkers"

    # Scoreboard Key:
    # "_" for Waiting for Connection
    # "S" for Starting up
    # "R" for Reading Request
    # "W" for Sending Reply
    # "K" for Keepalive (read)
    # "D" for DNS Lookup
    # "C" for Closing connection 
    # "L" for Logging
    # "G" for Gracefully finishing
    # "I" for Idle cleanup of worker
    # "." for Open slot with no current process

Installation
------------

 1. Download the scripts and move to your zabbix userscripts dir, i.e: /usr/lib/zabbix/externalscripts
 2. Run chmod +x on the files
 3. Add this to crontab: */5 * * * * /usr/bin/python /usr/lib/zabbix/externalscripts/fetch_apachestats.py <Webserver IP> <Webserver Port> &> /dev/null
 4. Replace Webserver IP and Port with your configuration and set the cron task to be executed in the interval of your own. Recomended lowest interval for your Zabbix checks.
 5. Add or uncomment this to your Apache config file:

        <Location /server-status>
         SetHandler server-status
         Order deny,allow
         Deny from all
         Allow from 127.0.0.1
         #Allow from <Zabbix proxy IP>
        </Location>
        ExtendedStatus On # Optional. Must be in global scope and not in a virtual host

 7. Remember to change 127.0.0.1 with your Zabbix server/proxy IP if you are planning to use it centralized. 
 8. Restart/reload Apache or use kill -USR1 `cat /var/run/httpd/httpd.pid` for zero downtime
 9. Load the azzbix template:  Apache-Template.xml
 10. Link the Template_Apache_HTTPd into the hosts in question. Remember that IP should match to configured in cron task
 11. Ensure Zabbix user has right permission on log file


 To use DNS names just modify the template to use DNS instead of {HOST.IP}.

License
-------

This template is distributed under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the  License, or (at your option) any later version.