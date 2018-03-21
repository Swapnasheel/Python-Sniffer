import struct

class TCP():
 
    def __init__(self, raw_data):
        self.src_port, self.dst_port, self.seq, self.ack, offset_reserved_flags = struct.unpack("! H H L L H", raw_data[:14])
        offset = (offset_reserved_flags >> 12) * 4
        self.urg = (offset_reserved_flags & 32) >> 5
        self.ack = (offset_reserved_flags & 16) >> 4
        self.push = (offset_reserved_flags & 8) >> 3
        self.rst = (offset_reserved_flags & 4) >> 2
        self.syn = (offset_reserved_flags & 2) >> 1
        self.fin = offset_reserved_flags & 1
        self.data = raw_data[offset:]
 
