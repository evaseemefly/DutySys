from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from CRM import models

# Create your views here.

#登录页面
def login(request):
    if request.method=="GET":
        return render(request,'login.html')
    elif request.method=="POST":
        #1判断是否存在指定用户
        #1.2 获取submit过来的username与pwd
        user=request.POST.get('username',None)
        pwd=request.POST.get('pwd',None)
        obj_user= models.UserInfo.objects.filter(username=user).first()
        if obj_user.pwd==pwd:
            return redirect('/index')
    #return HttpResponse()

