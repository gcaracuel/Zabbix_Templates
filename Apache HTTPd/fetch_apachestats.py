#!/usr/bin/python

""" Fetch Apache stats via mod_status from remote or local server. 
This program should act as daemon fetching mod_status regularly via cron task
By Guillermo Caracuel
Based on: https://www.zabbix.org/wiki/Docs/howto/apache_monitoring_script#Method_1

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import urllib
import os
import sys
import logging


#Configure logging
logfilename = '/var/log/zabbix/apachestats.log'
loggingLevel = logging.INFO

logging.basicConfig(filename=logfilename,level=loggingLevel,format='%(asctime)-15s %(levelname)-8s apachestats_daemon: %(message)s')


#logging.debug('This message should go to the log file')
#logging.info('So should this')
#logging.warning('And this, too')


# The web server IP to query
WebServer = sys.argv[1]

# Web server Port is the second argument
Port = sys.argv[2]

logging.info("Daemon asked to check " + sys.argv[1] + " " + sys.argv[2] )

# URL is hard coded to /server-status?auto but could be different in the future if needed
URL = "/server-status?auto"

# Set a sane default timeout (for all socket connections unfortunately...)
import socket
socket.setdefaulttimeout(3)

logging.debug("Timeout is 3 seconds")


############### Function to fire off an HTTP request to the web server, throw an exception gracefully 
############### and print FAIL if a connection can't be made


def getURL(WebServer,Port,URL):
    try:
        # Setup connection string
        ConnectionString = ("http://%s:%s%s") % (WebServer, Port, URL)

        logging.info("Trying to get stats from " + ConnectionString) 

        conn = urllib.urlopen(ConnectionString)
        URLresponse = conn.read()

        logging.debug("Response \n" + URLresponse)

        # Clean up the connection
        conn.close()

        # The response to the function is the output of the URL called
        return URLresponse

    # Catch all exceptions
    except:
        logging.Error("Error getting URL: " + ConnectionString)



#### Main body of script - Apache status is parsed and split into a list ####
TemporaryFileName = ("/tmp/%s.cache") % WebServer
TemporaryFile = open(TemporaryFileName, 'w')
TemporaryFile.write(getURL(WebServer,Port,URL))

logging.info("Apache stats fetched to file: " + TemporaryFileName)

# Close the file handle
TemporaryFile.close() 