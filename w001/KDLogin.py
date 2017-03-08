# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Ww2Zero
# Date: 2017/02/27
# Time: 11:06
# Blog: Ww2zero.github.io
# Function description
#
import ConfigParser
import os
import requests
import time
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class KDLogin(object):

    def __init__(self):
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,und;q=0.6',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': '192.168.255.66',
            'If-Modified-Since': 'Fri, 20 May 2016 07:17:01 GMT',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
        self.logoutURL = 'http://192.168.255.66/ajaxlogout?_t=1472292707672'
        self.loginURL = 'http://192.168.255.66/webAuth/'
        pass

    def getConfig(self, section, key):
        '''
         获取config配置文件
        '''
        config = ConfigParser.ConfigParser()
        path = os.path.split(os.path.realpath(__file__))[0] + '/set.conf'
        config.read(path)
        return config.get(section, key)

    def Logout(self):
        requests.get(self.logoutURL, headers=self.headers)
        print('上网账号注销成功')

    def Login(self, sectionid):

        # 构造Post数据
        postData = {
            'op': 'dmlogin', 'f': 'st', 'username': self.getConfig(
                sectionid, "Username").decode('gb2312'), 'password': self.getConfig(
                sectionid, "Password").decode('gb2312'), 'pwd': self.getConfig(
                sectionid, "Password").decode('gb2312'), 'secret': 'true'}

        r = requests.post(
            self.loginURL,
            data=postData,
            headers=self.headers)

        text = r.text

        print "正在登陆金证内网.."
        print "登陆的用户名为：" + self.getConfig(sectionid, "Username").decode('gb2312')
        if (len(text) > 600):
            if text.find("用户名和密码不能为空") > 0:
                print "登录失败;账号或是密码错误!"
                return
            print "恭喜 你登陆成功"
        print "2s后退出"
        time.sleep(2)

    def Main(self):
        print "请选择要登录的账号"
        print "----账号1------"
        print "内网账号：" + self.getConfig('weblogin1', "Username").decode('gb2312')
        print "----账号2------"
        print "内网账号：" + self.getConfig('weblogin2', "Username").decode('gb2312')
        time.sleep(1)
        i = input("请输入要登录的账号（1/2）:")
        self.Logout()
        if i == 1:
            self.Login('weblogin1')
        elif i == 2:
            self.Login('weblogin2')
        else:
            print "输入错误"
            print "正在退出.."
            time.sleep(1)
            exit()

if __name__ == '__main__':
    dk = KDLogin()
    try:
        dk.Main()

