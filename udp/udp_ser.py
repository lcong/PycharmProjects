import socket

import struct

BUFSIZ = 1024

ADDR = ('localhost', 2047)

recvsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    print 'waiting for the data'

    data,addr = recvsocket.recvfrom(BUFSIZ)

    print repr(data)

    (data1,) = struct.unpack('h', data)

    print repr(data1)

    (data2,) = struct.unpack('!h', data)

    print data2

recvsocket.close()