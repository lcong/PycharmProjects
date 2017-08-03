#!/usr/bin/python
# -*- coding:utf-8 -*-
from datetime import datetime

class myfile():

    def __init__(self, filepath):
        print('MyFile init...')
        self.filepath = filepath

    def printFilePath(self):
        print(self.filepath)

    def testReadFile(self):
        with open(self.filepath, 'r') as f:
            s = f.read()
            print('open for read...')
            print(s)

    def testWriteFile(self):
        with open('test.txt', 'w') as f:
            f.write('今天是 ')
            f.write(datetime.now().strftime('%Y-%m-%d'))


class item:
    def __init__(self):
        self.head = ''
        self.payload = ''
        self.name = ''

class lolist:
    def __init__(self,lol):
        self.lol= lol
        print('lol init...')

    def print_lol(self):
        for each_item in self.lol:
            if isinstance(each_item,list):
                lolist.print_lolist(each_item)
            else:
                print(each_item)
