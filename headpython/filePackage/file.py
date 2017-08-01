#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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