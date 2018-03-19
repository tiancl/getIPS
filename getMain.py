#coding:utf-8
"""
@author: tiancl
@version: 1.0
"""
import requests
from bs4 import BeautifulSoup
import lxml
from random import choice


num_url='https://www.v2ex.com/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36'}


list1=[]
splist=lambda seq,n:zip(*[iter(seq)]*n)
num_list=[]
ii=1
while len(num_list)<=10:
    try:
        url='https://www.kuaidaili.com/free/inha/%s/' % ii
        cont=requests.get(url,headers=headers)
        cont.encoding='utf-8'
        for i in BeautifulSoup(cont.text,'lxml').find('table',class_="table table-bordered table-striped").find_all("td"):
            list1.append(i.get_text())
        
        for j in list(splist(list1,7)):
            try:
                if requests.get(num_url,headers=headers,timeout=0.1).status_code==200:
                    num_list.append((j[0],j[1],j[3]))
            except Exception as e:
                print(e)
                continue
        list1.clear()
        ii+=1
    except Exception as e:
        print(e)
        break    
print(choice(num_list))