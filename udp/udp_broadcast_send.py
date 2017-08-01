#!/usr/bin/python
# -*- coding:utf-8 -*-

import socket, sys
import struct
str="080080076009f48c" #待发送的数据
str1=""
str2=""
str3=""
str4=""

addr = ('<broadcast>', 10000)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.sendto("hello from client", addr)

while str:
    str1=str[0:2] #分割字符串，获取前两个字符
    strto=int (str1,16)  #字符串转换成16进制
    str2+=struct.pack('B',strto) #转换成字节流，“B“为格式符，代表一个unsigned char （具体请查阅struct）
    str=str[2:]  #分割字符串，去掉字符串前两个字符

while (1):
    if (s.sendto(str2, addr)): pass  # UDP发送数据
    break

# data3 和data4赋予相同的数值
datavalue3=0x1516528
str3 =struct.pack('I',datavalue3) #转换成字节流，“I“为格式符，代表一个unsigned int （具体请查阅struct）

print "littel-endian str3"
print repr(str3)


while (1):
    if (s.sendto(str3, addr)): pass  # UDP发送数据
    break

datavalue4=0x1516528
str4 =struct.pack('!I',datavalue4) #转换成字节流，“I“为格式符，代表一个unsigned int （具体请查阅struct）


print "big-endian str4"
print repr(str4)



while (1):
    if (s.sendto(str4, addr)): pass  # UDP发送数据
    break

while 1:
    data = s.recvfrom(1024)
    if not data:
        break
    print data
