#!/usr/bin/env python
"""
AUTHOR
     
     guillermo.caracuel@optimaonline.es

LICENSE
 
    GPL
 
VERSION
 
    0.1
"""
 
import sys, os, traceback, argparse
import time
import re
import commands
 

#import logging
#import logging.handlers

def get_numtunnels():

    command =  "snmpget -c %s -v2c %s 1.3.6.1.4.1.9.9.171.1.3.1.1.0" % (args.community, args.IP)

    if args.verbose:
        print command

    try:   
        status, output = commands.getstatusoutput(command)

        if args.verbose: print output
    except Exception, e:
        print 'An error ocurred trying to execute the command'
        if args.verbose:
            print str(e)
            traceback.print_exc()
            os._exit(1) 

    # Parse tunnel IDs

    try:
        words = output.split()

        if args.verbose: print words

        if words[1] == "=":
            return int(words[3])
        else:   # Exit to trigger something
            print "No response or unknown response"
            os._exit(1) 
    except Exception, e:    # Exit to trigger something
        print "No response or unknown response"
        os._exit(1) 


 
def main ():
 
    global options, args
 
    # lLoging configuration to append to local syslog
    #my_logger = logging.getLogger('LogMigrator')
    #my_logger.setLevel(logging.INFO)
    #handler = logging.handlers.SysLogHandler(address = '/dev/log')
    #my_logger.addHandler(handler)
    #message = "SNMP_Tunnel_Check: %s %s %s %s " % (args.IP, args.community, args.tunnel, args.key)
    #my_logger.info(message)

        
    # Check key indicated
    
    if args.key == "IN-Bytes":
        OID = "1.3.6.1.4.1.9.9.171.1.3.2.1.26"
    elif args.key == "OUT-Bytes":
        OID = "1.3.6.1.4.1.9.9.171.1.3.2.1.39"
    elif args.key == "Uptime":
        OID = "1.3.6.1.4.1.9.9.171.1.3.2.1.10"
    else:   # Suposed key is Status
        OID = "1.3.6.1.4.1.9.9.171.1.3.2.1.51"

    command =  "snmpwalk -c %s -v 2c %s %s" % (args.community, args.IP,OID)

    if args.verbose:
        print command

    try:   
        status, output = commands.getstatusoutput(command)

        if args.verbose: print output
       
    except Exception, e:
        print 'An error ocurred trying to execute the command'
        if args.verbose:
            print str(e)
            traceback.print_exc()
            os._exit(1) 

    try:
        words = output.split()
        if args.verbose:
                print words

        if args.key == "IN-Bytes":
            num_tunnels = get_numtunnels()  
            if args.verbose:
                print num_tunnels
            sumarized=0
            for x in range(num_tunnels):
                index = 3+(x*4)
                sumatory = int(words[index])
                sumarized = sumarized + sumatory
            print sumarized
        elif args.key == "OUT-Bytes":  # For some reason SNMP return true value * 2 in OutOctects metrics
            num_tunnels = get_numtunnels()  
            if args.verbose:
                print num_tunnels
            sumarized=0
            for x in range(num_tunnels):
                index = 3+(x*4)
                sumatory = int(words[index])/2
                sumarized = sumarized + sumatory
            print sumarized
        else:   # Suposed key is Status or Uptime, es enough to return 1 value
            print words[3]
       
    except Exception, e:    # Exit to trigger something
        print "0"
        traceback.print_exc()
        os._exit(0) 
 
if __name__ == '__main__':
    try:
        start_time = time.time()
        parser = argparse.ArgumentParser(description='A python to be used as external check on Zabbix to get some parameters throught SNMP of Cisco routers. This script will replace the LLD SNMP discovery rule')
        parser.add_argument ('-v', '--verbose', action='store_true', default=False, help='verbose output')
        parser.add_argument ('IP', metavar='IP', action='store', help='Cisco Router IP')
        parser.add_argument ('community', metavar='community', action='store', help='SNMP community')
        parser.add_argument ('key', metavar='key to check', action='store', help='From list: [IN-Bytes, OUT-Bytes, Status, Uptime]')
        args = parser.parse_args()
        if args.verbose: print time.asctime()
        main()
        if args.verbose: print time.asctime()
        if args.verbose: print 'TOTAL TIME OF EXECUTION IN MINUTES:',
        if args.verbose: print (time.time() - start_time) / 60.0
        sys.exit(0)
    except KeyboardInterrupt, e: # Ctrl-C
        raise e
    except SystemExit, e: # sys.exit()
        raise e
    except Exception, e:
        print 'ERROR, UNEXPECTED EXCEPTION'
        print str(e)
        traceback.print_exc()
        os._exit(1)