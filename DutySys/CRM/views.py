from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

#登录页面
def login(request):
    return render(request,'login.html')
    #return HttpResponse()
