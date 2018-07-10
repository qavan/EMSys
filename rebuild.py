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
def unS(x):
    s=str(x)
    return re.sub(r' *$','',re.sub(r'^ *','',s))
#https://glosbe.com/gapi/translate?from=chv&dest=rus&format=json&phrase=савăн&pretty=true
g1ttru='https://glosbe.com/gapi/translate?from=tat&dest=rus&format=json&phrase='
g1ruch='https://glosbe.com/gapi/translate?from=rus&dest=chv&format=json&phrase='
g2='&pretty=false'
d1='https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=dict.1.1.20180710T072536Z.a7dafd610cdabf2b.8499fb6d6fe6a4c151b685067b4998e33c104b0e'
p='&text='
d2='&lang=tt-ru'
#line='кунак,курс,кунакханә,купе,купорос,курай,кура,курган,кургаш,кургашын,курку,куркыныч,куркынычсызлык,курорт,куртка,куруш,курчак,курьер,кустар,куфараз,кухня,кучкар,кушак,кушылдык,кушымта'
#L=line.split(',')
hs = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 YaBrowser/18.4.0.1387 (beta) Yowser/2.5 Safari/537.36'} 
def yandexdict(pair,word):
    global hs
    d1='https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=dict.1.1.20180710T072536Z.a7dafd610cdabf2b.8499fb6d6fe6a4c151b685067b4998e33c104b0e'
    p='&text='
    if pair=='tt-ru':
        d2='&lang=tt-ru'
    else:
        d2='&lang=ru-tt'
    r=requests.get(d1+p+word+d2,headers=hs)
    jy=json.loads(r.text)
    jy=jy['def']
    yd=[]
    for e in range(len(jy)):
        yttru=re.findall(r'\'text\'\: \'[а-яөәҗңү]*\'\, \'pos\'\: \'noun\'\,',str(jy[e]))
        for f in range(len(yttru)):
            yttru[f]=re.sub(r'[^а-яөәҗңү]{2,15}','',yttru[f])
        for f in range(len(yttru)):
            yd.append(yttru[f])
    #print(yd)
    return [word,yd]
def glosbe(p1,p2,word):
    global hs
    u1='https://glosbe.com/gapi/translate?'
    u2='&format=json&phrase='
    u3='&pretty=false'
    u='from='+p1+'&dest='+p2
    r=requests.get(u1+u+u2+word+u3,headers=hs)
    jsonDate = json.loads(r.text)
    s=jsonDate['tuc']
    for x in range(len(s)):
        t=re.sub(r'\, \'meanings\'\: \[\{\'[a-z]*\'\: \'[a-z]*\'\, \'[a-z]*\'\: \'.*\'\}\]','',str(s[x]))
        t=re.sub(r'(\-)?[0-9]*','',t)
        t=re.sub(r'[[a-z\'{}:\[\-\]]*','',t)
        t=re.sub(r' {2,100}','',t)
        t=re.sub(r'\,\, I \,','',t)
        s[x]=t
    #print(s)
    return [word,s]
def inc(word='куркыныч'):
    t1=yandexdict('tt-ru',word)
    t2=glosbe('tat','rus',word)
    if t1[1]==[] and t2[1]==[]:
        temp=[]
    elif t1[1]==[] and t2[1]!=[]:
        temp=t2[1]
    elif t1[1]!=[] and t2[1]==[]:
        temp=t1[1]
    else:
        temp=[]
        for x in range(len(t1[1])):
            temp.append(t1[1][x])
        for x in range(len(t2[1])):
            status=False
            for y in range(len(temp)):
                if temp[y]==t2[1][x]:
                    status=True
                    break
            if status==False:
                temp.append(t2[1][x])
    db=[word,temp]
    chv=[]#for ready trios: tat#chv#rus
    dix=[]#ready bidix
    rus=[]#not translated at chv rus words
    for x in range(len(db[1])):
        cv=glosbe('rus','chv',db[1][x])
        if len(cv[1])==0:
            rus.append(db[1][x])
        status=True
        for y in range(len(cv[1])):
            chv.append(db[0]+'###'+cv[1][y]+'###'+db[1][x])
            dix.append('<f>'+cv[1][y]+'<s>'+db[0]+'<t>')
        #print(cv)
    #print(rus)
    #print(chv)
    #print(db)
    for i in range(len(rus)):
        print(rus[i])
    for i in range(len(dix)):
        print(dix[i])
def tatpoisk(word):
    global hs                                                             #preparation
    u='http://tatpoisk.net/dict/'                                         #
    r=requests.get(u+word,headers=hs)                                     #
    soup=BeautifulSoup(r.text,"lxml")                                     #
    
    sr=soup.find('p',{'class':'search_results'})                          #getting of block with translations
    try:
        head=sr.find('b')                                                 #translated words parsing from html re-tag
        tr_list=re.findall(r'\<i\>.*\<\/p\>',str(sr))                     #
        
    except:                                                               #
        print('WE or DDCT')                                               #
        tp=[]                                                             #returns empty list when "tatpoisk" doesnt have translation for requested word
        return tp                                                         #
    
    if len(tr_list)==1:                                                   #if intranslate 1 kind lexc
        if len(tr_list[0].split('.'))>1 and str(tr_list[0]).find('#')==-1:#if more then 1 translation
            trs=tr_list[0].split('.')                                     #split by steps
            trs.pop(0)                                                    #del first elem because he have just trash for us
            
            for x in range(len(trs)):                                     #
                trs[x]=re.sub(r'\d','',trs[x])                            #delete all numerals from text
                trs[x]=unS(trs[x])                                        #unSpace left and right sides of list elements(translations)
                
                if str(trs[x]).find(', ')!=-1:                            #
                    templ=trs[x].split(', ')                              #split unity strings by ", " for getting more translations
                    trs[x]=templ[0]                                       #
                    for y in range(len(templ)-1):                         #
                        trs.append(templ[y+1])                            #
                        
            trs[len(trs)-1]=unS(unHTML(str(trs[len(trs)-1])))             #replace "p" tag in last word in list
            
            for x in range(len(trs)):                 
                if str(trs[x]).find('//')!=-1:                            #split by "//"
                    templ=trs[x].split('//')                              #
                    trs[x]=templ[0]                                       #
                    for y in range(len(templ)-1):                         #
                        trs.append(templ[y+1])                            #
            print(trs)
        elif len(tr_list)==1:                                                     #if 1 translation
            tr_list[0]=unS(unHTML(str(re.sub(r'\<i\>.*\<\/i\>','',tr_list[0]))))  #delplace "i"... tag
            templ=tr_list[0].split('//')                                          #split by "//"
            if len(templ)>1:                                                      #
                tr_list[0]=templ[0]                                               #
                for n in range(len(templ)-1):                                     #
                    tr_list.append(unS(templ[n+1]))                               #
            print(tr_list)                                                        #
            
tatpoisk('кура')
#куркынычсызлык

