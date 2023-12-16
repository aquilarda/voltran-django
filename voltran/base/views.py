from django.shortcuts import render


def home(request):
    return render(request, 'base/home.html')


def members(request):
    return render(request, 'base/members.html')


def log(request):
    return render(request,'base/log.html')