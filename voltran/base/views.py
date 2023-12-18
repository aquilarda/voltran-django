from django.shortcuts import render
from base.models import Member, Project, Log


def home(request):
    members = Member.objects.all()
    context = {"members": members}
    return render(request, 'base/home.html', context)


def members(request):
    return render(request, 'base/members.html')


def log(request):
    return render(request,'base/log.html')