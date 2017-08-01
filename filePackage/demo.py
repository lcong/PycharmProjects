from demo.classOne import classOne
from demo.classTwo import classTwo
from demo.file import myfile
from demo.file import item
import struct
import binascii
import ctypes



if __name__ == "__main__":
    c1 = classOne()
    c1.printInfo()

    c2 = classTwo()
    c2.printInfo()

    a = myfile("./demo/test.txt")
    a.printFilePath()
    a.testReadFile()

    b=item() # 定义结构对象
    b.head = 0x08
    b.payload= 0x10
    b.name = "cup"



    data=struct.pack("ih",b.head,b.payload)

    print(repr(data))

    values = [0x08,0x20,0x12]

    data1 = struct.pack("iiI", 0x08,0x20,0x12345678)

    print(repr(data1))


    print('------------0----------------')

    values = (1, b'abc', 2.7)
    s = struct.Struct('I3sf')
    packed_data = s.pack(*values)
    unpacked_data = s.unpack(packed_data)
    print('Original values:', values)
    print('Format string :', s.format)
    print('Uses :', s.size, 'bytes')
    print('Packed Value :', binascii.hexlify(packed_data))
    print('Unpacked Type :', type(unpacked_data), ' Value:', unpacked_data)
    print('------------1----------------')

    values = (1, b'abc', 2.7)
    s = struct.Struct('I3sf')
    prebuffer = ctypes.create_string_buffer(s.size)
    print('Before :', binascii.hexlify(prebuffer))
    s.pack_into(prebuffer, 0, *values)
    print('After pack:', binascii.hexlify(prebuffer))
    unpacked = s.unpack_from(prebuffer, 0)
    print('After unpack:', unpacked)


    print('-------------2---------------')
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
