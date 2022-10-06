from django.http import HttpResponse, HttpResponseRedirect

from django.template import loader
from .models import importData
from django.urls import reverse

def func(request):
    dt = importData.objects.all().values()
    temp = loader.get_template("index.html")

    dic = {"data":dt}

    return HttpResponse(temp.render(dic, request))

def add(request):
     temp = loader.get_template("add.html")
     return HttpResponse(temp.render({}, request))

def addnum(request):
    x = request.POST["one"]
    y = request.POST["two"]
    z = float(x)+float(y)
    num = importData(numone = x, numtwo = y, result = z)
    num.save()
    return HttpResponseRedirect(reverse("index"))


def clear(request):
    dt = importData.objects.all()
    dt.delete()
    return HttpResponseRedirect(reverse("index"))
