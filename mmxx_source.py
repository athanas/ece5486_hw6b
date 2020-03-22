#!/usr/bin/env python
import socket
from time import sleep
from random import random
from math import log

# Mean value of the arrival rate of packets
LAMBDA = 120.0   # packets per second
CUSTOMERS = 2000 # total # of packets sent through system
                 # some will get blocked

# Model the exponential distribution generator
def exp_delay(x):
    return -log(1.0 - random())/x

# Generate packets and broadcast them to the LAN
sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
server_address = ('255.255.255.255', 10000)

print("Starting.  Sending "+str(CUSTOMERS)+" packets for processing.")
for i in range(0, CUSTOMERS):
    sock.sendto(str(i)+0*'-',server_address)
    sleep(exp_delay(LAMBDA))
    if i & 0xffffffc0 == i: print(str(i)+" packets sent.")

# Signal that we are done.
sleep(1)
for i in range(0,30): sock.sendto('stop',server_address)
print("Done.")

