#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#address=('127.0.0.1',10000)
host='127.0.0.1'
port=10000

s.bind((host,port))
while 1:
 data,addr=s.recvfrom(2048)
 if not data:
  break
 print "got data from",addr
 print data
s.close()