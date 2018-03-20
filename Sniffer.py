import struct
import socket

from network.ethernet import Ethernet
from network.ipv4 import IPv4


TAB1 = '\t - '
TAB2 = '\t\t - '
TAB3 = '\t\t\t - '
TAB4 = '\t\t\t\t - '


def Main():

    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
 
    for i in range(0,5):
    #while True:
        raw_data, addr = conn.recvfrom(65530)
        eth = Ethernet(raw_data)
        print("-----------------------------------------------------------------------------------------------------")
        print("ETHERNET:")
        print(TAB1 + "Destination mac: {}, Source mac: {}, Protocol: {}".format(eth.dest_mac, eth.src_mac, eth.proto))

        ## IP packets, check proto value
        if eth.proto == 8:
            ipv4 = IPv4(eth.data)
            print('\n' + TAB1 + "IPV4:")
            print(TAB2 + "Source IP: {}, Destination IP: {}".format(ipv4.src_ip, ipv4.dst_ip))
            print(TAB2 + "Version: {}, Header length: {}".format(ipv4.version, ipv4.header_length))
            print(TAB2 + "TTL: {}, Protocol: {}".format(ipv4.ttl, ipv4.proto))
            #print(TAB2 + "Data: {}".format(ipv4.data))
            print("-----------------------------------------------------------------------------------------------------")





Main()

        







