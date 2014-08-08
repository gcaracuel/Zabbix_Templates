Jboss Template
=================

Zabbix Jboss template using JMX. See: https://www.zabbix.com/documentation/2.4/manual/config/items/itemtypes/jmx_monitoring

Items
-----

  * <TO-DO>
   
Triggers
--------

  * <TO-DO>

Graphs
------

  * <TO-DO>


Installation
------------

1. Configure your JBOSS server to listen JMX
  Edit:  "$JBOSS_HOME/bin/run.conf" to add:

        JAVA_OPTS="$JAVA_OPTS -Dcom.sun.management.jmxremote.port=9010" 
        JAVA_OPTS="$JAVA_OPTS -Dcom.sun.management.jmxremote.ssl=false" 
        JAVA_OPTS="$JAVA_OPTS -Dcom.sun.management.jmxremote.authenticate=false"

  This will open a listening optin in port 9010 for JMX
  or: 

        JAVA_OPTS="$JAVA_OPTS -Djava.rmi.server.hostname=192.168.1.xxx"
        JAVA_OPTS="$JAVA_OPTS -Dcom.sun.management.jmxremote"
        JAVA_OPTS="$JAVA_OPTS -Dcom.sun.management.jmxremote.port=9010"
        JAVA_OPTS="$JAVA_OPTS -Dcom.sun.management.jmxremote.authenticate=true"
        JAVA_OPTS="$JAVA_OPTS -Dcom.sun.management.jmxremote.password.file=/etc/java-6-openjdk/management/jmxremote.password"
        JAVA_OPTS="$JAVA_OPTS -Dcom.sun.management.jmxremote.access.file=/etc/java-6-openjdk/management/jmxremote.access"
        JAVA_OPTS="$JAVA_OPTS -Dcom.sun.management.jmxremote.ssl=false"


2. Open your your firewall to allow JMX connections. 
  Your would need too open RMI protocol to create the conection. Unfortunelly this protocol use random ports 49152:65535. You could solve it following this tutorial: http://olegz.wordpress.com/2009/03/23/jmx-connectivity-through-the-firewall/
  But if not, just open it, i.e in iptables:

        -A RH-Firewall-1-INPUT -m state --state NEW -m tcp -p tcp --dport 9010 -j ACCEPT
        -A RH-Firewall-1-INPUT -m state --state NEW -m tcp -p tcp --dport 49152:65535 -j ACCEPT

  or a more secure way... open that ports just for your Zabbix Java gateway

        -A RH-Firewall-1-INPUT -m state --state NEW -m tcp -s <your-zabbix-java-gateway-ip> -p tcp --dport 9010 -j ACCEPT
        -A RH-Firewall-1-INPUT -m state --state NEW -m tcp -s <your-zabbix-java-gateway-ip> -p tcp --dport 49152:65535 -j ACCEPT

3- Install a Zabbix Java Gateway

    yum install zabbix-java-gateway
    chkconfig zabbix-java-gateway on

  Edit: /etc/zabbix/zabbix_java_gateway.conf adding:

    LISTEN_IP="0.0.0.0"
    LISTEN_PORT=10052
    START_POLLERS=10

    service zabbix-java-gateway start

    netstat -an | grep 10052

  Open port in iptables:

    -A INPUT -p tcp -m state --state NEW -m tcp --dport 10052 -j ACCEPT

4- Connect your zabbix server/proxy to this Zabbix Java Gateway editing your /etc/zabbix/zabbix_server.conf or /etc/zabbix/zabbix_proxy.conf

    JavaGateway=localhost
    JavaGatewayPort=10052
    StartJavaPollers=5

5- Load the template and let's monitor girls!

License
-------

This template is distributed under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the  License, or (at your option) any later version.