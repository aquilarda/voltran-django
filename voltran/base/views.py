from django.shortcuts import render
from base.models import Member, Project, Log


def home(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, 'base/home.html', context)


def members(request):
    members = Member.objects.all()
    context = {"members": members}
    return render(request, 'base/members.html', context)


def log(request):
    logs = Log.objects.all()
    context = {"logs": logs}
    return render(request,'base/log.html', context)