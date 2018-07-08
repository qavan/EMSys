#!/usr/bin/env python3.5
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
def normalize(x):
    stroka=re.sub(r'[\000-\377]*', lambda m:''.join([chr(ord(i)) for i in m.group(0)]).decode('utf8'),x)
    return stroka
def unHTML(x):
    s=re.sub(r'\<[^>]*\>', '',x)
    return s
TAT=[]
def tatpoisk(a):
    global TAT
    TAT=[]
    u=[str(a)]
    u1='http://tatpoisk.net/dict/'
    hs = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 YaBrowser/18.4.0.1387 (beta) Yowser/2.5 Safari/537.36'}
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
                    print('Ct1')#нестандартная разметка
                    continue
            else:
                if len(re.findall(r'\#',tl))<1:
                    tlt=re.sub(r'[0-9]\.','#',tl)
                    tlt=str(tlt).split(' # ')
                    pray=[]
                    for e in range(len(tlt)):
                        if len(tlt[e].split(', '))==2:
                            ptr=tlt[e].split(', ')
                            tlt[e]=ptr[0]
                            tlt.append(ptr[1])
                        if len(tlt[e].split(' // '))==2:
                            ptr=tlt[e].split(' // ')
                            tlt[e]=ptr[0]
                            tlt.append(ptr[1])
                        if str(tlt[e]).find(' ')!=-1:
                            pray.append(tlt[e])
                    for e in range(len(tlt)):
                        if len(tlt[e].split(' // '))==2:
                            ptr=tlt[e].split(' // ')
                            tlt[e]=ptr[0]
                            tlt.append(ptr[1])
                    for e in range(len(pray)):
                        tlt.remove(pray[e])
                    for m in range(len(tlt)):
                        tlt[m]=re.sub(r'^ *','',tlt[m])
                        tlt[m]=re.sub(r' *$','',tlt[m])
                    tlt.pop(0)
                    TAT.append(str(u[x]))
                    TAT.append(tlt)
                    print(TAT)
                else:
                    print('Ct2')#нестандартная разметка
                    continue

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
                        print('Ct3')#нестандартная разметка
                        continue
            else:
                print('Ct4')#нестандартная разметка
                continue
            
            for m in range(len(tlt)):
                tlt[m]=re.sub(r'^ *','',tlt[m])
                tlt[m]=re.sub(r' *$','',tlt[m])            
            TAT.append(str(u[x]))
            TAT.append(tlt)

y1='https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20180707T071801Z.01d16d3db0de1be8.828886d473350c85dfbaa2db499a7826fa7e40d0&text='
y2='&lang=ru-tt'
#https://glosbe.com/gapi/translate?from=chv&dest=rus&format=json&phrase=савăн&pretty=true
g1ttru='https://glosbe.com/gapi/translate?from=tat&dest=rus&format=json&phrase='
g1ruch='https://glosbe.com/gapi/translate?from=rus&dest=chv&format=json&phrase='
g2='&pretty=false'
u1='https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20180707T071801Z.01d16d3db0de1be8.828886d473350c85dfbaa2db499a7826fa7e40d0'
p='&text='
u2='&lang=ru-tt'
line='ярату,абажур,үлем,әҗәл'
L=line.split(',')
ttbyout=[]
ttpyout=[]
ttsyout=[]
ttryout=[]
GTT=[]
GCV=[]
hs = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 YaBrowser/18.4.0.1387 (beta) Yowser/2.5 Safari/537.36'}
for i in range(0,len(L)):
    url=g1ttru+str(L[i])+g2
    tatpoisk(str(L[i]))
    print(url)
    r=requests.get(url,headers=hs)
    #res=re.findall(r'(\[\{)?\"[а-яәөңҗү]{2,1000}\"(\}\])?',r.content)
    jsonDate = json.loads(r.text)
    s=jsonDate['tuc']
    for x in range(len(s)):
        t=re.sub(r'\, \'meanings\'\: \[\{\'[a-z]*\'\: \'[a-z]*\'\, \'[a-z]*\'\: \'.*\'\}\]','',str(s[x]))
        t=re.sub(r'(\-)?[0-9]*','',t)
        t=re.sub(r'[[a-z\'{}:\[\-\]]*','',t)
        t=re.sub(r' {2,100}','',t)
        t=re.sub(r'\,\, I \,','',t)
        s[x]=t
#        print(s[x])
    x=0
    print(s)
    while x<=len(s)-1:
        #print(s[x])
        if s[x].find(',')!=-1:
            s.remove(str(s[x]))
            x-=1
        x+=1
    if s==[]:
        print('C1')#нет рез-ов тат=рус
        continue
    tlist=[]
    tt=tlist.copy()
    tt.append(str(L[i]))
    tt.append(s)
#
    yandextemp=[]
    p='&text='
    temp=p+str(tt[0])
    url=u1+temp+u2
    r=requests.get(url,headers=hs)
    print(url)
    par=re.sub(r'[h]','@',r.text)
    par=re.sub(r'[a-z0-9-":}{[]]*','',par)
    par=re.sub(r'(,,)','',par)
    par=re.sub(r'@','h',par)
    ty=par.split(',')
    tempya=[]
    #print(tt)
    for j in range(len(ty)-1):
        if  str(ty[j]).find('%')!=-1:
            ttpyout.append(tt[0])
        elif str(ty[j]).find(' ')!=-1:
            ttsyout.append(tt[0])
        elif (str(ty[j]).find('ө')!=-1 or str(ty[j]).find('ә')!=-1 or str(ty[j]).find('җ')!=-1 or str(ty[j]).find('ң')!=-1 or str(ty[j]).find('ү')!=-1) and ty[y]!=str(tt[0]) :
            ttbyout.append(tt[0])
        elif ty[j]==str(tt[0]):
            ttrout.append(tt[0])
        else:
            tempya.append(str(ty[j]))
    for j in range(len(tempya)-1):
        stat=False
        for x in range(len(tt)-1):
            if str(tt[1][x])==str(tempya[j]):
                stat=True
        if stat!=True:
            tt[1].append(str(tempya[j]))
    if TAT!=[]:
        ##print(TAT)
        for w in range(len(TAT[1])):
            print(TAT[1][w])
            tt[1].append(TAT[1][w])
        #tt[1].append(TAT[1][0:])
###
###
    #print(tt)
    #print(tt)
    for j in range(len(tt[1])):#-1
        url=g1ruch+str(tt[1][j])+g2
        #print(str(tt[1][j]))
        r=requests.get(url,headers=hs)
        print(url)
        jsonDate = json.loads(r.text)
        s=jsonDate['tuc']
        #print(s)
        for y in range(len(s)):
            #print(s[y])#"meanings":[{"language":"ru","text":"&#39;&#39;поэтич. тж.&#39;&#39; passion"}]
            #jsonDate=json.loads(str(s[y]))
            #rlk=jsonDate['meanings']
            #print(rlk)re.sub(r'\, \'meanings\'\: \[\{\'[a-z]*\'\: \'[a-z]*\'\, \'[a-z]*\'\: \'.*\'\}\]','',r)
            t=re.sub(r'\, \'meanings\'\: \[\{\'[a-z]*\'\: \'[a-z]*\'\, \'[a-z]*\'\: \'.*\'\}\]','',str(s[y]))
            t=re.sub(r'(\-)?[0-9]*','',t)
            t=re.sub(r'[[a-z\'{}:\[\-\]]*','',t)
            t=re.sub(r' {2,100}','',t)
            t=re.sub(r'\,\, I \,','',t)
            s[y]=t
            #print(t)
        x=0
        while x<=len(s)-1:
            #print(s[x])
            if s[x].find(',')!=-1:
                s.remove(str(s[x]))
                x-=1
            x+=1
        if s==[]:
            print('C2')#нету рез-ов рус-чув
            continue
        ch=tlist.copy()
        ch.append(str(tt[1][j]))
        ch.append(s)
    try:
        if ch!=[] and s!=[]:
            GTT.append(tt)
            GCV.append(ch)
    except NameError:
        print('NE')
#for x in range(len(tt)-1):
#    for y in range(len(ch[1])-1):#<e><p><l>   <s n="n"/></l><r>   <s n="n"/></r></p></e>
#        print('<e><p><l>'+ch[1][y]+'<s n="n"/></l><r>'+tt[0]+'<s n="n"/></r></p></e>')
#for x in range(len(ch[1])-1):
#    print(ch[1][x]+':'+ch[1][x]+'           temp;!""')
##print(GTT)
##print(GCV)
#print()
#for x in range(len(GTT)-1):
#    for y in range(len(GTT[x][2])-1):
#        for z in range(len(GCV[y][2])-1):
#            print('<e><p><l>'+GCV[y][2][z]+'<s n="n"/></l><r>'+GCV[x][2][y]+'<s n="n"/></r></p></e>')
#        print(GTT[x][y]+':'+GTT[x][y]+'           temp;!""')
#        print('<e><p><l>'+GCV[x][y]+'<s n="n"/></l><r>'+GCV[x][y]+'<s n="n"/></r></p></e>')

for y in range(len(GTT)):
    for z in range(len(GCV[y][1])):
        print('<e><p><l>'+GCV[y][1][z]+'<s n="tempT"/></l><r>'+GTT[y][0]+'<s n="tempT"/></r></p></e>')

for x in range(len(GCV)):
    for y in range(len(GCV[x][1])):
        pp=0
        print(GCV[x][1][y]+':'+GCV[x][1][y]+'           tempT;!""')
        

































    
    

