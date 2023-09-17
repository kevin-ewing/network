from scapy.all import *
import sys


for i in range(1, 28):
    pkt = IP(dst=sys.argv[1], ttl=i) / UDP(dport=33434)
    
    # Send the packet and get a reply
    reply = sr1(pkt, verbose=0)
    if reply is None:
        # No reply =(
        break
    elif reply.type == 3:
        # We've reached our destination
        print("Destination reached: ", reply.src)
        break
    else:
        # We're in the middle somewhere
        print("%d: " % i , reply.src)