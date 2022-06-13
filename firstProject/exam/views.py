from django.shortcuts import render
from django.http import HttpResponse
def showTest(request):
    que="Who developed c language"
    a="Ken Thomson"
    b="Danis Ritchi"
    c="Bjarm Trostraf"                        
    d="sanket takale"
    level="Easy"
    data={'que':que,'a':a,'b':b,'c':c,'d':d,'level' :level }
    res=render(request,'exam/Test.html',context=data)
    return res
def showResult(request):
    s="<h1>showResult page<h1/>"
    return HttpResponse(s)
