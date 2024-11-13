from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import product
# Create your views here.

def e_com_login(req):
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['password']
        shop=authenticate(username=uname,password=password)
        if shop:
            login(req,shop)
            return redirect(shop_home)
        else:
            messages.warning(req,'invalid username or password')
            return redirect(e_com_login)
    else:
        return render(req,'login.html')
    

def e_com_logout(req):
    logout(req)
    return redirect(e_com_login)

def e_com_addpro(req):
    return render(req,'shop/add.html')

def shop_home(req):
    products=product.objects.all()
    return render(req,'shop/home.html',{'products':products})


# std=[{'roll_no':'1','name':'sanju','age':25},{'roll_no':'2','name':'anju','age':23}]
def add(req):
    if req.method=='POST':
        pid=req.POST['pid']
        name=req.POST['name']
        dis=req.POST['dis']
        price=req.POST['price']
        offer_price=req.POST['offer_price']
        stock=req.POST['stock']
        std.append({'pid':pid,'name':name,'dis':dis})
        print(std)
        return redirect(add)
    else:
        return render(req,'add_std.html',{'std':std})  
