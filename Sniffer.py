import struct
import socket

from network.ethernet import Ethernet
from network.ipv4 import IPv4
from network.icmp import ICMP
from network.tcp import TCP


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
        print("NEW PACKET:")
        print("- ETHERNET:")
        print(TAB1 + "Destination mac: {}, Source mac: {}, Protocol: {}".format(eth.dest_mac, eth.src_mac, eth.proto))

        ## IP packets, check proto value eq 8
        if eth.proto == 8:
            ipv4 = IPv4(eth.data)
            print('\n' + TAB1 + "IPV4:")
            print(TAB2 + "Source IP: {}, Destination IP: {}".format(ipv4.src_ip, ipv4.dst_ip))
            print(TAB2 + "Version: {}, Header length: {}".format(ipv4.version, ipv4.header_length))
            print(TAB2 + "TTL: {}, Protocol: {}".format(ipv4.ttl, ipv4.proto))

            ## ICMP packets if protocol = 1
            if ipv4.proto == 1:
                icmp = ICMP(ipv4.data)
                print("\n" + TAB2 + 'ICMP:')
                print(TAB3 + "Icmp_type: {}, Code: {}, Checksum: {}".format(icmp.icmp_type, icmp.code, icmp.checksum))
                print(TAB3 + "ICMP DATA: {}".format(icmp.data)) 
                print("-----------------------------------------------------------------------------------------------------")
      
            ## TCP Packets if protocol = 6
            elif ipv4.proto == 6:
                tcp = TCP(ipv4.data)
                print("\n" + TAB2 + "TCP:")
                print(TAB3 + "Source Port: {}, Destination Port: {}".format(tcp.src_port, tcp.dst_port))
                print(TAB3 + "Acknowledge: {}, Sequence_number: {}".format(tcp.ack, tcp.seq))
                print(TAB3 + "Flags:\n" + TAB3 + "Urgent: {}, Ack: {}, Push: {}, Rst: {}, Syn: {}, Fin: {}".format(tcp.urg, tcp.ack, tcp.push, tcp.rst, tcp.syn, tcp.fin))
                print(TAB3 + "TCP_DATA: {}".format(tcp.data))
                print("-----------------------------------------------------------------------------------------------------")
 
            ## UDP Packets if protocol = 17



Main()

        







