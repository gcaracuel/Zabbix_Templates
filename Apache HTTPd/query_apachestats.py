#!/usr/bin/python

""" Query Apache stats via mod_status from a cached values. 
This check script should work together with the daemon to download mod_status regularly
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

import csv
import sys
import os
import logging


#Configure logging
logfilename = '/var/log/zabbix/apachestats.log'
loggingLevel = logging.INFO

logging.basicConfig(filename=logfilename,level=loggingLevel,format='%(asctime)-15s %(levelname)-8s apachestats_query: %(message)s')

# The web server IP to query
WebServer = sys.argv[1]

# Metric the user is asking for
RequestedMetric = sys.argv[2]

logging.info("Request received to check " + sys.argv[2] + " for " + sys.argv[1] )

########################################################################
### This function deals with "ordinary" metrics, such as CPULoad etc ###
########################################################################

def GetMetric(RequestedMetric):
  
    for index in range(0, 9):
        if RequestedMetric == ServerStatusOutput[index][0]:
            return ServerStatusOutput[index][1]

    logging.error("Metric requested "+ RequestedMetric +" not found, returning [ZBX_NOTSUPPORTED] to Zabbix...")
    return "[ZBX_NOTSUPPORTED]"

    # Standard Key:
    # "Total Accesses"
    # "Total kBytes"
    # "CPULoad" This metric is not always present, take care
    # "Uptime"
    # "ReqPerSec"
    # "BytesPerSec"
    # "BytesPerReq"
    # "BusyWorkers"
    # "IdleWorkers"



###################################################################
### This function deals with specifically the Apache scoreboard ###
###################################################################

# function to count the metric requested... used in every if statement
def GetScoreboardMetric(RequestedMetric):
    logging.debug("Asked for a scoreboard metric... " + RequestedMetric)
    
    # Check if resquested metric match a valid state for workers
    if not RequestedMetric in "_SRWKDCLGI.":
        logging.error("Metric requested not found, returning [ZBX_NOTSUPPORTED] to Zabbix...")
        return "[ZBX_NOTSUPPORTED]"

    # initialize counter variable
    RequestedMetricCount = 0

    # Some mod_status don't answer for CPULoad so this index may change
    if ServerStatusOutput[8][0] == "Scoreboard":
        index = 8
    else:
        index = 9

    # iterate over the ScoreBoard part and count the number of the requested metric
    for CountMetric in ServerStatusOutput[index][1]:
        if CountMetric == RequestedMetric:
            RequestedMetricCount = RequestedMetricCount + 1 
    return RequestedMetricCount

    # Scoreboard Key:
    # "_" Waiting for Connection, 
    # "S" Starting up, 
    # "R" Reading Request,
    # "W" Sending Reply, 
    # "K" Keepalive (read), 
    # "D" DNS Lookup,
    # "C" Closing connection, 
    # "L" Logging, 
    # "G" Gracefully finishing,
    # "I" Idle cleanup of worker, 
    # "." Open slot with no current process


TemporaryFileName = ("/tmp/%s.cache") % WebServer

logging.debug("Trying to open " + TemporaryFileName)

try:
    # Parse the CSV file we just wrote
    CSVReader = csv.reader(open(TemporaryFileName, "rb"), delimiter = ":", skipinitialspace=True)
except:
    logging.error("File not found, maybe mod_status fetcher not working properly, take a look to logs" + TemporaryFileName)
    print "[ZBX_NOTSUPPORTED]" 
    sys.exit(1)

logging.debug("Trying to split CSV from " + TemporaryFileName )

# Turn the split CSV into a two dimensional list
ServerStatusOutput = []
for Metric in CSVReader:
    ServerStatusOutput.append(Metric)

try:
    # if the last argument to the script is more than two characters, this means an "ordinary" metric was asked for
    if len(RequestedMetric) > 2:
        logging.info("Trying to fetch metric " + RequestedMetric )
        print GetMetric(RequestedMetric)

    # Otherwise print the Scoreboard specific metric
    else:
        logging.info("Trying to fetch metric from scoreboard  " + RequestedMetric )
        print GetScoreboardMetric(RequestedMetric)
except:
    logging.error("Metric requested not supported, returning [ZBX_NOTSUPPORTED] to Zabbix...")
    print "[ZBX_NOTSUPPORTED]"