# Returns formatted mac addr

def get_mac_addr(mac):
    byte_str = map('{:02x}'.format, mac)
    return ':'.join(byte_str).upper()


