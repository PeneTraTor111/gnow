from django.shortcuts import render
from django.shortcuts import HttpResponse
import sqlite3
from index.models import gameInfo,gRadio
# Create your views here.

def index(request):
    updateGradio()
    return render(request, "myindex.html",{'gameInfo': gameInfo, 'radio':gRadio})

def result(request):
    updateGameInfo()
    lis = ["HTML", "CSS", "jQuery", "Python", "Django"]
    count = len(lis)
    return render(request, "result.html", {'lis': lis, 'count':count, 'gameInfo': gameInfo})

def content(request):
    introduction = "《塞尔达传说》系列首部登陆任天堂Switch主机的作品，本作也是系列第一款开放世界作品，玩家可以脱出此前的各种限制，在广阔的世界中自由探索。 游戏故事依然是林克拯救世界的故事，海拉尔大陆再次被加农侵袭，林克从长眠中醒来，在冒险中获得武器、能力，最后去挑战加农。但你也可以直接去干掉加农，本作的自由度是系列前所未有的。 在《塞尔达传说 旷野之息》中，林克从一开始就获得了所有道具能力，并且可以和世界中的各种要素进行互动。大自然的风火雷电都可以被利用，让林克的冒险有层出不穷的玩法。 本作中文版将于2018年2月1日推出，中文版标题确认为《塞尔达传说：旷野之息》。"
    return render(request, "content.html", {'data': introduction})

def search(request):
    msg = request.GET.get('search')
    '''if not msg:
        return render(request, "./")'''
    lis = ["HTML", "CSS", "jQuery", "Python", "Django"]
    count = len(lis)
    return render(request, "result.html", {'lis': lis, 'count': count})

def updateGameInfo():
    PATH_TO_DB = "../price.db"
    conn = sqlite3.connect(PATH_TO_DB)
    cursor = conn.cursor()
    cursor.execute('select * from gameprice')
    result = cursor.fetchall()
    for game in result:
        name = game[0]
        allprice = []
        for price in game[1:]:
            allprice.append(float(price))
        bestprice = 0
        for i in allprice:
            bestprice = bestprice if bestprice > i else i
        gameinfo = gameInfo(name=name, description='',bestPrice=bestprice,bestPriceCounty='')
        gameinfo.save()
    cursor.close()
    conn.close()

def updateGradio():
    PATH_TO_DB = "../price.db"
    conn = sqlite3.connect(PATH_TO_DB)
    cursor = conn.cursor()
    cursor.execute('select * from radio')
    result = cursor.fetchall()
    for radio in result:
        head = radio[0]
        time = radio[1]
        href = radio[2]
        imgSrc = radio[3]
        imgTitle = radio[4]
        describe = radio[5]
        gradio = gRadio(head=head,time=time,href=href,imgSrc=imgSrc,imgTitle=imgTitle,describe=describe)
        gradio.save()
    cursor.close()
    conn.close()