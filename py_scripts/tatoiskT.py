# -*- coding: utf-8 -*-
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
import re
import requests
import time
import json
from lxml import html
from bs4 import BeautifulSoup
def unHTML(x):
    s=re.sub(r'\<[^>]*\>', '',x)
    return s
hs = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 YaBrowser/18.4.0.1387 (beta) Yowser/2.5 Safari/537.36'}
u1='http://tatpoisk.net/dict/'
u=['мәхәббәт','новый']
TAT=[]
for x in range(len(u)):
    r=requests.get(u1+str(u[x]),headers=hs)
    soup=BeautifulSoup(r.text,"lxml")
    ptatp=soup.find('p',{'class':'search_results'})
    try:
        head=unHTML(str(ptatp.find('b')))
    except AttributeError:
        print('AE')
        continue
    iz=ptatp.find_all('i')
    if len(re.findall(r'\-',unHTML(str(ptatp))))==1:
        tl=re.sub(r'.* \-','',unHTML(str(ptatp)))
        tl=unHTML(str(ptatp))[len(str(u[x]))+3:]
        if len(iz)==1:
            if len(re.findall(r'\#',tl))<1:
                tlt=tl.split(',')
            else:
                tlt0=tl.split('#')
                tlt=tlt0[0].split(',')
            if len(iz)>0:
                tlt[0]=tlt[0].split(' ')[1]
            else:
                continue
        else:
            if len(re.findall(r'\#',tl))<1:
                tlt=tl.split(',')
            else:
                continue
        pek=[]
        r=pek.copy()
        r.append(str(u[x]))
        r.append(tlt)
        print(r)
        TAT.append(r)
    else:
        tl=unHTML(str(ptatp))[len(str(u[x]))+3:]
        #print(tl)
        if len(re.findall(r'\#',tl))<1:
            tlt=tl.split(',')
        else:
            tlt0=tl.split('#')
            tlt=tlt0[0].split(',')
        if len(iz)>0:
            tlt[0]=tlt[0].split(' ')[2]
            for m in range(len(tlt)):
                tlt[m]=re.sub(r'\(.*\)','',tlt[m])
                if str(tlt[m]).find(';')!=-1:
                    temple=str(tlt[m]).split(';')
                    tlt[m]=temple[0]
                    for p in range(len(temple)-1):
                        tlt.append(temple[p+1])
                else:
                    continue
        else:
            continue
        pek=[]
        r=pek.copy()
        r.append(str(u[x]))
        for m in range(len(tlt)):
            tlt[m]=re.sub(r'^ *','',tlt[m])
            tlt[m]=re.sub(r' *$','',tlt[m])
        r.append(tlt)
        print(r)
        #    if str(tlt[m]).find(';')!=-1:
        TAT.append(r)
print(TAT)

    
