## Unpack IPv4 pakcets

import socket, struct

class IPv4():

    def __init__(self, raw_data):
        version_header_length = raw_data[0]
        self.version = version_header_length >> 4
        self.header_length = (version_header_length & 15) * 4
        self.ttl, self.proto, src_ip, dst_ip = struct.unpack("! 8x B B 2x 4s 4s", raw_data[:20])
        self.src_ip = self.ipv4(src_ip)
        self.dst_ip = self.ipv4(dst_ip)
        self.data = raw_data[self.header_length:]

    # Returns formatted IP
    def ipv4(self, ip):
        return ".".join(map(str, ip))


