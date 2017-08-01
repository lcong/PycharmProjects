#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from filePackage import myfile

if __name__ == '__main__':
    a = myfile("./filePackage/test.txt")
    a.printFilePath();
    a.testReadFile();