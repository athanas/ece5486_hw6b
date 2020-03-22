#!/usr/bin/env python
import socket
import os

CUSTOMERS = 2000

# Create a sink for absorbing packets from the processor(s)
sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 10001))

pkt_count = 0
fp = open(os.path.expanduser('~')+'/Desktop/processed_pkts.txt','w')
print("Starting")
while True:
    data, address = sock.recvfrom(1024)
    print("Rcvd "+data)
    if 'stop' in data: break
    fp.write("Packet "+data+" rcvd from "+address[0]+'\n')
    pkt_count += 1

fp.write("Done. "+str(pkt_count)+" pkts out of "+str(CUSTOMERS)+" received.\n")
fp.close()

