import struct
import socket

from network.ethernet import Ethernet


TAB1 = '\t - '


def Main():

    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    while True:
        raw_data, addr = conn.recvfrom(65530)
        eth = Ethernet(raw_data)

        print("\nEthernet frame:")
        print(TAB1 + "Destination mac: {}, Source mac: {}, Protocol: {}".format(eth.dest_mac, eth.src_mac, eth.proto))


Main()

        







