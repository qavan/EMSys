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
hs = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 YaBrowser/18.4.0.1387 (beta) Yowser/2.5 Safari/537.36'} 
###$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
###$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
###$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
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
    global counter
    counter+=1
    global hs
    u1='https://glosbe.com/gapi/translate?'
    u2='&format=json&phrase='
    u3='&pretty=false'
    u='from='+p1+'&dest='+p2
    r=requests.get(u1+u+u2+word+u3,headers=hs)
    try:
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
    except:
        print('captcha?')
        input()
        return [word,[]]
###$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
###$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
###$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def tatpoisk(word):
    global hs                                                             #preparation
    u='http://tatpoisk.net/dict/'                                         #
    r=requests.get(u+word,headers=hs)                                     #
    soup=BeautifulSoup(r.text,"lxml")                                     #
    
    sr=soup.find('p',{'class':'search_results'})                          #getting of block with translations
    #print(sr)
    try:
        head=sr.find('b')
        if len(re.findall(r'\<i\>.*\<\/p\>',str(sr)))==0:
            tr_list=re.findall(r'\<\/a\>.*\<\/p\>',str(sr))
            tr_list[0]=re.sub(r' \- ','',unHTML(str(tr_list[0])))
            #print(tr_list)
        else:
            tr_list=re.findall(r'\<i\>.*\<\/p\>',str(sr))
    except:
        print('WE or DDCT')
        tp=[]
        return tp                                                         #
    #print(sr)
    #print(tr_list)
    if len(tr_list[0].split('.'))>1 :                 #if intranslate 1 kind lexc
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
            return trs
        #elif len(tr_list[0].split(','))>1 and str(tr_list[0]).find('#')==-1:
        #    trs=tr_list[0].split(',')                                     #split by steps
        #    trs.pop(0)                                                    #del first elem because he have just trash for us  
        elif len(tr_list)==1:                                                     #if 1 translation
            #print('here')
            tr_list[0]=unS(unHTML(str(re.sub(r'\<i\>.*\<\/i\>','',tr_list[0]))))  #delplace "i"... tag
            templ=tr_list[0].split('//')                                          #split by "//"
            if len(templ)>1:                                                      #
                tr_list[0]=templ[0]                                               #
                for n in range(len(templ)-1):                                     #
                    tr_list.append(unS(templ[n+1]))                               #
            return tr_list                                                        #

    elif  len(tr_list)==1 and len(tr_list[0].split('.'))==1:
        tr_list[0]=unS(unHTML(str(re.sub(r'\<i\>.*\<\/i\>','',tr_list[0]))))
        templ=tr_list[0].split('//')
        if len(templ)>1:                                                      #
            tr_list[0]=templ[0]                                               #
            for n in range(len(templ)-1):                                     #
                tr_list.append(unS(templ[n+1]))                               #
        return tr_list                                                      #
#ls=tatpoisk(input())#кура
#print(ls)
#куркынычсызлык
#for x in range(len(L)):
#    print(L[x])
#    ls=tatpoisk(L[x])
#    for y in range(len(ls)):
#        ls[y]=re.sub(r'(\(.*\)?(\<\/p\>)?)','',str(ls[y]))
#    print(ls)
###$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
###$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
###$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
chv=[]#for ready trios: tat#chv#rus
dix=[]#ready bidix
rus=[]#not translated at chv rus words
line='аам,сабандаш,сабанчы,сабах,саботаж,сабыйлык,сабырлылык,сабырсызлык,саванна,савап,савымчы,сага,сагалак,сагыз,сагызак,сагынмалык,садак,садака,садакачы,садәлек,садизм,садист,садистлык,саескан,сажин,сазан,сазанак,сазлык,сазчы,саилче,саилчелек,сай,сайланучанлык,сайланыш,сайлык,сака,сакалбай,сакаулык,саквояж,саклагыч,сакля,сакма,сакман,саксофон,саксызлык,сакчыллык,сакчылык,салака,саламандра,салат,салатчы,салдат,салкынлык,салкынчалык,салмаклык,салон,салфетка,салынкылык,сальдо,салют,самавырчы,самак,саман,самбо,самбочы,самимилек,самимият,самовар,самогон,самогончы,самодержавие,самокат,самолёт,самум,самур,самурай,самшит,санак,саналмыш,санамыш,санаторий,сангвиник,сандал,сандали,сандыкчы,санәм,санитария,санитарка,санитарлык,санскрит,сансызлык,сантехник,сантехника,сантим,сантиметр,сантиметрлык,сантый,сантыйлык,санузел,санчасть,саңак,саңгыраулык,сапёр,саплам,саплаяк,саплык,сапма,сапсан,сапфир,сар,саравыч,сарана,саранча,сарафан,сарацин,сараяк,сарбай,саргылтлык,сарделька,сардин,сардина,сардоникс,саржа,сари,сарказм,саркастик,саркома,саркофаг,саркынды,саркыт,сармак,сармат,сарпинка,сару,сарут,сарыбаш,сарыкчылык,сарылык,сарыф,сарыч,сасык,сасыкай,сасылык,сателлит,сатин,сатир,сатирачы,саткын,сатрап,сатылучанлык,сауләт,сауна,саусызлык,саутия,сафари,сафлор,сафлык,сафсата,сафсатачы,сахабә,сахароза,сахиб,сахра,сахтыян,сач,сбор,сбруй,сварка,сваркачы,сварщик,свастика,светофор,свеча,свита,свитер,сеанс,себергеч,себерке,себерле,сегмент,сегрегация,сезонлылык,сейм,сейнер,сейсмик,сейсмограф,сейсмолог,сейсмология,сейф,секанс,секвойя,секрет,секретариат,секретарьлык,секреция,секс,сексология,сексопатология,секстан,секстант,секстет,сексуальлек,секта,сектант,сектантлык,секундант,секундомер,селектор,селекционер,селекция,селен,селенит,селәгәй,селәү,селәүсен,селәүчән,селитра,селкенеш,селкенмә,селкенчәк,селте,селтелелек,сельдерей,сельдь,селькор,сельмаг,сельпо,семантика,семасиология,семафор,семестр,семәк,семинарист,семинария,семиотика,семит,семья,семьялык,сенаторлык,сенбернар,сенсация,сенсор,сенсуализм,сентиментализм,сентименталист,сентиментальлек,сеньор,сеньора,сеньорита,сеңелкәй,сеңерчә,сеңле,сепарат,сепаратизм,сепаратист,сепаратор,сепаратчы,сепарация,сепсис,септет,септик,септима,серб,сербияле,сервант,сервер,сервиз,сердәш,сердәшлек,сердәшче,серенада,сержантлык,сериал,серия,серкә,серкәлек,серкәч,серлелек,сероводород,серотерапия,серпантин,серрият,сертотмас,сестра,сетка,сәбәплелек,сәбәпчелек,сәбәт,сәвер,сәвәләй,сәвәт,сәгатьчелек,сәдакать,сәдәп,сәдәф,сәел,сәерлек,сәйлән,сәйран,сәйранлык,сәйяр,сәйях,сәке,сәкен,сәкәл,сәламәтсезлек,сәләтлек,сәләтлелек,сәләтсезлек,сәләхият,сәма,сәмавилек,сәмәрә,сәмруг,сәнгатьлелек,сәнгатьче,сәнгатьчелек,сәнгатьчәлек,сәнгатьчәнлек,сәндерә,сәнәга,сәнәк,сәнәкче,сәратан,сәргаскәр,сәргаскәрлек,сәргәрдан,сәрдәлек,сәркәтип,сәрләүхә,сәрмая,сәрхуш,сәрхушлек,сәт,сәтыр,сәүдәгәрлек,сәүдәчелек,сәүмәт,сәфәрдәш,сәфәрче,сәхабә,сәхәр,сәхрә,сәхтиян,сәясәтчелек,сәясилек,сәяхәтнамә,сәяхәтчелек,сёмга,сигара,сигнализатор,сигнализация,сигналчы,сизгерлек,сизүчәнлек,сикелтә,сикергеч,сикерем,сикертмә,сикәлтә,сил,силә,силос,силуэт,симбиоз,символизм,символика,символист,симезлек,симметрия,симметриялелек,симпатия,симпозиум,симптом,симулянт,симуляция,симфония,синагога,сингармонизм,сингармония,синдикат,синдром,синекдоха,синергетика,синергизм,синкретизм,синод,синолог,синология,синонимика,синонимия,синоптика,синтагма,синтаксис,синтаксист,синтезатор,синтетика,синус,синусоида,синхрония,синхронлык,синхрофазотрон,синьор,синьора,сионизм,сионист,сипкел,сипкеч,сиптергеч,сират,сирена,сирень,сирәклек,сирияле,сироп,сиртмә,сиртмәкойрык,системалык,системалылык,системасызлык,ситсы,сифон,сихерлек,сихерче,сихерчелек,сихәт,сихәтлек,сихрилек,сият,скакалка,скальп,скальпель,скандинавияле,сканер,скарлатина,скат,скафандр,скважина,сквер,скелет,скептик,скептиклык,скептицизм,скетч,скипетр,скипидар,скит,скиф,склад,складчы,склероз,скрепер,скреперчы,скрипкачы,скульптор,скульптура,скумбрия,славистика,славянофил,славянчылык,слайд,слалом,сланец,следователь,слесарь,слесарьлык,слёт,слива,словак,словен,слюда,смета,смог,смокинг,смотр,снайпер,снайперлык,снаряд,снобизм,собор,советник,советчы,советчылык,совинформбюро,совнарком,совнархоз,совхозчы,согуд,сода,сол,солан,солдатлык,солдафон,солидарлык,солидол,солитер,соло,солтанат,солтанлык,солыбаш,солыхнамә,солыча,солычык,соль,сольфеджио,солянка,соляр,солярий,солярка,соната,сонатина,сонет,соңгылык,сопа,сопка,сопрано,соран,соранчы,сораулык,сорбит,соргавыл,сорка,сорнай,сорнайчы,сорт,сортировка,сортлылык,сорыкорт,сорыкортлык,сорылык,соса,сосиска,соскы,сосла,сослан,сословие,сословиечелек,сотник,соус,софа,софист,софистика,сохари,сохбәт,социал,социал%-демократ,социал%-демократия,социализация,социалист,социалист%-революционер,социолог,социологизм,соцстрах,сочинение,союздашлык,союзник,соя,сөек,сөзге,сөзгеч,сөзәклек,сөйдергеч,сөйкем,сөйкемлелек,сөйләк,сөйләүлек,сөймән,сөйрәк,сөйрәткеч,сөкә,сөлекче,сөлтәр,сөм,сөмбаш,сөмбелә,сөмсезлек,сөмсер,сөннәтче,сөннәтчелек,сөңге,сөңгече,сөрем,сөренте,сөрән,сөрәнче,сөркә,сөрткеч,сөрүлек,сөрхәнтәй,сөт%-катык,сөтлегән,сөтче,сөтчелек,сөючәнлек,сөяк%-санак,сөякче,сөян,сөяркә,спазм,спазма,спартакиада,спартан,спектроскоп,спектроскопия,спекулянт,спекулянтлык,спекуляция,сперма,специализация,специалист,спецовка,спидометр,спиннинг,спираль,спонсор,спортзал,спортклуб,спортсмен,спринт,спринтер,спрут,спутник,ссуда,стабилизатор,стабильлек,ставка,ставрида,стадия,стайер,сталагмит,сталинизм,сталинист,стан,стандартизация,станица,становой,станокчы,стапель,староста,старосталык,стартер,стартчы,старшиналык,статут,стахановчы,стахановчылык,ствол,стеарин,стела,стеллаж,стенгазета,стенд,стенка,стенограмма,стенография,стенокардия,стержень,стерилизация,стерлинг,стетоскоп,стилист,стиляга,стимул,стимулятор,стипендиат,стихия,стихиялелек,столбняк,столяр,стоматолог,стоматология,стопа,стражник,стратег,стратосфера,страхование,стрелка,стрептомицин,стрептоцид,стресс,стриптиз,стронций,строфа,струк,студентлык,стюард,стюардесса,суалчан,суанасы,суасты,суахили,субай,субстанция,субтитр,субуяр,субъективизм,субъективлык,сувенир,суверенитет,суверенлашу,суверенлык,суворовчы,суганча,сугымлык,сугымчы,сугышчанлык,суданлы,судночылык,судьялык,суеш%-кырылыш,сузылучанлык,суицид,сукай,сукачы,сукбай,сукбайлык,суккыч,сукно,сукырлык,сулагайлык,суллык,сулылык,сулышлык,сульфит,сума,сумала,сумса,суна,сунар,сунарчы,супа,супергигант,суперйолдыз,суперкубок,супермен,супертышлык,суперүткәргеч,сур,сургыч,сурәтче,сурәтчелек,сурик,суррогат,сусак,сусаклагыч,сусызлык,сусыллык,сусын,сут,сутый,суүлчәгеч,суүлчәр,суүсем,суүткәргеч,суфизм,суфилык,суфичылык,суфле,суффикс,суфыйлык,суфыйчылык,сухта,сучы,сушка,сушки,суыклык,суыргыч,суырткыч,суыткыч,сүзбәйләнеш,сүзлекчелек,сүзлекчә,сүзче,сүзчәнлек,сүл,сүләмә,сүлпәнлек,сүндергеч,сүр,сүрек,сүрәкә,сүрү,сүс,сүсән,сфинкс,схематиклык,схемачылык,сходка,схоласт,схоластика'
L=line.split(',')
counter=0
for i in range(len(L)):
    if i%15==0:
        print(i)
    t1=yandexdict('tt-ru',str(L[i]))
    t2=glosbe('tat','rus',str(L[i]))
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
    db=[str(L[i]),temp]
    for x in range(len(db[1])):
        cv=glosbe('rus','chv',db[1][x])
        if len(cv[1])==0:
            rus.append(db[1][x])
        status=True
        for y in range(len(cv[1])):
            chv.append(db[0]+'###'+str(cv[1][y]).replace(' ','% ')+'###'+db[1][x])
            dix.append('<f>'+str(cv[1][y]).replace(' ','<b/>')+'<s>'+db[0]+'<t>')
for i in range(len(rus)):
    print(rus[i])
for i in range(len(chv)):
    if str(chv[i]).find(',')==-1:
        print(chv[i])
for i in range(len(dix)):
    if str(dix[i]).find(',')==-1:
        print(dix[i])