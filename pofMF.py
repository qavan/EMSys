# -*- coding: utf-8 -*-
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
import re
import requests
import time
from lxml import html
from bs4 import BeautifulSoup
alf=['a','aa','b','v','g','d','e','zh','j','z','i','iy','k','l','m','n','o','oo','p','r','s','t','u','y','f','x','h','ch','sh','ii','ee','yu','ya']
#alf=['k','aa']
def normalize(x):
    stroka=re.sub(r'[\000-\377]*', lambda m:''.join([chr(ord(i)) for i in m.group(0)]).decode('utf8'),x)
    return stroka
def unHTML(x):
    s=re.sub(r'\<[^>]*\>', '',x)
    return s
def unHTML(x):
    s=re.sub(r'\<[^>]*\>', '',x)
    return s
count=0
bl='http://magarif-uku.ru/tatar-isemnere/kyz/'
listok=[]

bl='http://magarif-uku.ru/tatar-isemnere/ir-at/'
for i in range(len(alf)-1):
    url=bl+str(alf[i])
    print(url)
    hs = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 YaBrowser/18.4.0.1387 (beta) Yowser/2.5 Safari/537.36'}
    r=requests.get(url,headers=hs)
    soup=BeautifulSoup(r.content,"lxml")
    #f=open('s1','w')
    #f.write(table)
    #f.close()
    table=soup.find('tbody')
    #print(table)
    #print(len(table))#page.find_all('strong',{'class':' phr'})
    #print('S')
    tr=table.find_all('tr')
    for x in range(4,len(tr)-1):
        #print(tr[x])
        tds=tr[x].find_all('td')#,{'width','192'}
        #print(tds)
        #print('#')
        #print(unHTML(str(tds[0])))
        #print('#')
        #print(unHTML(str(tds[4])))
        try:
            listok.append(unHTML(str(tds[0]))+'#'+unHTML(str(tds[4]))+'#'+'M')
            count+=1
        except IndexError:
            print('IndexError')
    print(count)
print('count= '+str(count))
for x in range(len(listok)-1):
    print(str(listok[x]))
print('res= '+str(result))




