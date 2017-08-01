import socket

import struct

BUFSIZ = 1024

ADDR = ('localhost', 2047)

sendsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = struct.pack('!I', 14)

print "big-endian"
print repr(data)

data = struct.pack('I', 14)

print "little-endian"

print repr(data)

sendsocket.sendto(data, ADDR)

sendsocket.close()