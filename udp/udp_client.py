#!/usr/bin/python
# -*- coding:utf-8 -*-

import socket
addr=('127.0.0.1',10000)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print ">>>>>>>>"
while 1:
 data=raw_input()
 if not data:
  break
 s.sendto(data,addr)
s.close()