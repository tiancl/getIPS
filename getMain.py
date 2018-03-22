#coding:utf-8
"""
@author: tiancl
@version: 1.0
"""
import requests
from bs4 import BeautifulSoup
import lxml
from random import choice

"""
param：
timeout:可自定义修改
targeturl：可自定义修改为爬取网站
使用方法：
ips=getIP()
ips.getProxies()
proxies=ips.proxies
"""
class getIP(object):
    def __init__(self):
        self.tag=1      #页数
        self.timeout=2  #超时时间
        self.findurl="https://www.kuaidaili.com/free/inha/"  #获取ip网站
        self.targeturl='https://www.baidu.com/'   #需要爬取的网站
        #消息头
        self.headers= {'User-Agent':'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36'}
        self.proxies={}
        self.iplist=[]
        self.splist=lambda seq,n:zip(*[iter(seq)]*n)
    
    def getProxies(self):
        while len(self.proxies)==0:
            self.sourceurl=self.findurl+'%s/' % self.tag
            cont=requests.get(self.sourceurl,headers=self.headers)
            for i in BeautifulSoup(cont.text,'lxml').find('table',class_="table table-bordered table-striped").find_all("td"):
                self.iplist.append(i.get_text())
            for j in list(self.splist(self.iplist,7)):
                self.proxies['%s'%j[3]]='%s://%s:%s' % (j[3],j[0],j[1])
                if requests.get(self.targeturl,headers=self.headers,timeout=self.timeout,proxies=self.proxies).status_code==200:
                    break
                self.proxies.clear()  
            self.tag+=1

if __name__=='__main__':
    ips=getIP()
    ips.getProxies()
    print(ips.proxies)