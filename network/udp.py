import struct

class UDP():

    def __init__(self, raw_data):

        self.src_port, self.dst_port, self.length = struct.unpack("! H H 2x H", raw_data[:8])
        self.data = raw_data[8:]
