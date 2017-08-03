#!/usr/bin/python
# -*- coding:utf-8 -*-
from demo.classOne import classOne
from demo.classTwo import classTwo
from demo.file import myfile
from demo.file import item,lolist
import struct
import binascii
import ctypes



if __name__ == "__main__":

    print("class1 demo 的演示调用")
    c1 = classOne()
    c1.printInfo()

    print("class2 demo 的演示调用")
    c2 = classTwo()
    c2.printInfo()

    print("class file demo 的演示调用")
    a = myfile("./demo/test.txt")
    a.printFilePath()
    a.testReadFile()
    a.testWriteFile()

    print("class item demo 的演示调用")
    b=item() # 定义结构对象
    b.head = 0x08
    b.payload= 0x10
    b.name = b"a cup of coffee"


    data0=struct.pack("ih10s", b.head, b.payload, b.name)
    print('data0 Values :', binascii.hexlify(data0))

    values = [0x08,0x20,0x12]
    data1 = struct.pack("iih",*values)
    print('data1 Values :', binascii.hexlify(data1))

    print('------------第“1”种打包方式----------------')

    values = (1, b'abc', 2.7)
    s = struct.Struct('I3sf')
    packed_data = s.pack(*values)
    unpacked_data = s.unpack(packed_data)
    print('Original values:', values)
    print('Format string :', s.format)
    print('Uses :', s.size, 'bytes')
    print('Packed Value :', binascii.hexlify(packed_data))
    print('Unpacked Type :', type(unpacked_data), ' Value:', unpacked_data)


    print('------------第“2”种打包方式----------------')

    values = (1, b'abc', 2.7)
    s = struct.Struct('I3sf')
    prebuffer = ctypes.create_string_buffer(s.size)
    print('Before :', binascii.hexlify(prebuffer))
    s.pack_into(prebuffer, 0, *values)
    print('After pack:', binascii.hexlify(prebuffer))
    unpacked = s.unpack_from(prebuffer, 0)
    print('After unpack:', unpacked)


    print('------------第“3”种打包方式----------------')

    values1 = (1, b'abc', 2.7)
    values2 = (b'defg', 101)
    s1 = struct.Struct('I3sf')
    s2 = struct.Struct('4sI')

    prebuffer = ctypes.create_string_buffer(s1.size + s2.size)
    print('Before :', binascii.hexlify(prebuffer))
    s1.pack_into(prebuffer, 0, *values1)
    s2.pack_into(prebuffer, s1.size, *values2)
    print('After pack:', binascii.hexlify(prebuffer))
    print(s1.unpack_from(prebuffer, 0))
    print(s2.unpack_from(prebuffer, s1.size))


    print('我们来看python的list处理机制')
    movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
                    ["Graham Chapman", ["Michael Palin", "John Cleese",
                        "Terry Gilliam", "Eric Idle", "Terry Jones"]]]


    def print_lol(a_list,indent=True,level=0):
        for each_item in a_list:
            if isinstance(each_item, list):
                print_lol(each_item,indent,level+1)
            else:
                if indent:
                    for l in range(level):
                        print("\t", end='')
                print(each_item)


    print_lol(movies,1)

