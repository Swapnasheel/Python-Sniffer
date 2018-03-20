#!/usr/bin/python3.6

import struct
import socket

tab_1 = '\t - '
tab_2 = '\t\t - '
tab_3 = '\t\t\t - '
tab_4 = '\t\t\t\t - '


def main():
    conn = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.ntohs(3))

    while True:
        raw_data, addr = conn.recvfrom(65535)
        dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)
        print("Ethernet Frame..")
        print("Destination: {}, Source: {}, Protocol: {}".format(dest_mac, src_mac, eth_proto))


## Unpack the ethernet frame 
def ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
    return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[14:]

def get_mac_addr(mac):
    byte_str = map('{:02x}'.format, mac)
    return ':'.join(byte_str).upper()


## Unpack the IP frame
def ipv4_packet(data):
    version_header_length = data[0]
    version = version_header_length >> 4
    header_length = (version_header_length & 15) * 4
    ttl, proto, src_ip, dst_ip = struct.unpack("! 8x B B 2x 4S 4S", data[:20])
    return version, header_length, ttl, proto, ipv4(src_ip), ipv4(dst_ip), data[header_length:]

def ipv4(data):
    return '.'.join(map(str, data))


## Unpack ICMP Packets based on the protocol numbers
def icmp_packet(data):
    icmp_type, code, checksum = struct.unpack('! B B H ', data[:4])
    return icmp_type, code, checksum, data[4:]

## Unpack TCP Packets based on the protocol numbers
def tcp_packets(data):
    (src_port, dst_port, seq, ack, offset_reserved_flags) = struct.unpack("! H H L L H", data[:14])
    offset = (offset_reserved_flags >> 12) * 4



if __name__ == '__main__':
    main()
