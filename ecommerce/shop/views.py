from django.shortcuts import render,redirect
from django.http import HttpResponse
from shop.models import category,Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def allcategories(request):
    c=category.objects.all()
    return render(request,'category.html',{'c':c})

def allproducts(request,p):
    c=category.objects.get(name=p)
    p=Product.objects.filter(category=c)
    return render(request,'product.html',{'c':c,'p':p})

def detail(request,p):
    p=Product.objects.get(name=p)
    return render(request,'detail.html',{'p':p})

def register(request):
        if (request.method=="POST"):
            u=request.POST['u']
            p=request.POST['p']
            cp=request.POST['cp']
            f=request.POST['f']
            l=request.POST['l']
            e = request.POST['e']

            if (p==cp):
                user=User.objects.create_user(username=u, password=p, first_name=f, last_name=l, email=e)
                user.save()
                return redirect('shop:allcat')
            else:
                return HttpResponse("Password are not same")
        return render(request, 'register.html')


def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('shop:allcat')
        else:
            return HttpResponse("Invalid Credentials")
    return render(request,'login.html')


def user_logout(request):
    logout(request)
    return redirect('shop:login')