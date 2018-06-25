from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def index(request):
    return render(request, "myindex.html")

def result(request):
    lis = ["HTML", "CSS", "jQuery", "Python", "Django"]
    count = len(lis)
    return render(request, "result.html", {'lis': lis, 'count':count})

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