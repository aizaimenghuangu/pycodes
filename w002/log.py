#-*- coding:utf8 -*-

__author__ = 'Wwzero'
#
# MTA BP日志sql简单提取工具
# 提取入参
# 提取sql
#

import os
import time


def scanlog(logpath):
    fi = open(logpath)
    fo = open("MTAlog.sql", "w")
    line = fi.readline()
    start = time.time()
    while line:
        line = line[line.find(']:') + 2:]
        # print(line)
        # 提取入参信息
        if line.find(':') > 0:
            if line.find('=') < 0 and line.find('sql:') < 0 and line.find('KJSE JROS') < 0:
                # print(line)
                # fo.write('\n')
                fo.writelines("--" + line)
        # 提取sql
        if line.find("exec sql:") > 0:
            if line.find("rpc=") < 0:
                line = line[line.find('sql:') + 4:]
                # print(line)
                # fo.write('\n')
                fo.writelines("--" + line)
        line = fi.readline()
    fo.close()
    fi.close()
    c = time.time() - start
    print('times is :%0.2f' % (c))


def scaninsert():
    fi = open("MTAlog.sql")
    fo = open("MTAInsertLog.sql", 'w')
    line = fi.readline()
    start = time.time()
    while line:
        # 提取入参信息
        if line.find(':') > 0:
            # print(line)
            # fo.write('\n')
            fo.writelines("-" + line)
        # 提取sql
        if line.find("insert") > 0 and line.find("into") > 0:
            # print(line)
            # fo.write('\n')
            fo.writelines("-" + line)
        line = fi.readline()
    fo.close()
    fi.close()
    c = time.time() - start
    print('times is :%0.2f' % (c))


def main():
    print(u'----MTA BP日志sql提取工具----')
    #logpath = raw_input(u"请输入sql日志的路径：".encode("gbk"))
    logpath = u"F:\\MTA\\svnloc\\kcbp\\bin\\log\\user\\20170206\\User_data0.log"
    scanlog(logpath)  # 提取sql
    scaninsert()      # 提取insert

if __name__ == '__main__':
    main()
