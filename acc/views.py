from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from .models import User
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, "acc/index.html")

def chpass(request):
    u = request.user
    cp = request.POST.get("cpass")
    if check_password(cp, u.password):
        np = request.POST.get("npass")
        u.set_password(np)
        u.save()
        return redirect("acc:login")
    else:
        messages.error(request, "잘못된 접근입니다")
    return redirect("acc:update")

def update(request):
    if request.method == "POST":
        u = request.user
        um = request.POST.get("umail")
        up = request.FILES.get("upic")
        uc = request.POST.get("ucomm")
        if up:
            u.pic.delete()
            u.pic = up
        u.email , u.comment = um, uc
        u.save()
        return redirect("acc:profile")
    return render(request, "acc/update.html")

def signup(request):
    if request.user.is_authenticated:
        messages.warning(request, '로그아웃 해주세요.')
        return redirect("acc:index")

    if request.method == "POST":
        un = request.POST.get('uname')
        up = request.POST.get("upass")
        uc = request.POST.get("ucomm")
        ua = request.POST.get("uage")
        pic = request.FILES.get("upic")
        try:
            User.objects.create_user(username=un, password=up, comment=uc, age=ua, pic=pic)
            return redirect("acc:login")
        except:
            pass # 마지막
    return render(request, "acc/signup.html")


def delete(request):
    u = request.user
    cp = request.POST.get("cpass")
    if check_password(cp, u.password):
        u.pic.delete()
        u.delete()
        return redirect("acc:index")
    return redirect("acc:profile")


def ulogin(request):
    if request.user.is_authenticated:
        messages.warning(request, '이미 로그인 했습니다.')
        return redirect("acc:index")
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        u = authenticate(username=un, password=up)
        if u:
            login(request, u)
            messages.success(request, f"{u} 님 환영합니다!")
            return redirect("acc:index")
        else:
            messages.info(request, '계정 정보가 일치하지 않습니다')
    return render(request, "acc/login.html")


def ulogout(request):
    logout(request)
    return redirect("acc:index")


def profile(request):
    if request.user.is_anonymous:
        messages.warning(request, '로그인 해주세요.')
        return redirect("acc:login")
    return render(request, "acc/profile.html")