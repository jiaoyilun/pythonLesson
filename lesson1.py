# -*- coding: utf-8 -*-
import os


def readfile():
    filename = "E:/test.txt";
    if os.path.exists(filename):
        file = open(filename, 'r', encoding='utf-8')
        lines = file.readlines()
        for ln in lines:
            print(ln)
        file.close
    else:
        print("文件不存在")


readfile()
