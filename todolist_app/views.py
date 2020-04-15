from django.shortcuts import render ,redirect
from django.http import HttpResponse ,HttpRequest
from todolist_app.models import TaskList
def todolist(request):
    alltask= TaskList.objects.all()
    return render(request, 'todolist.html',{'alltask':alltask})





def csxii(request):
    onetask= TaskList.objects.filter(subject_name='Computer Science') & TaskList.objects.filter(Class_name='XII')
    context= {'csxii':'Class-XII Topics ','alltask':onetask}
    return render(request, 'csxii.html',context)


def csxi(request):
    onetask= TaskList.objects.filter(subject_name='Computer Science') & TaskList.objects.filter(Class_name='XI')
    context= {'csxii':'Class-XI Topics ','alltask':onetask}
    return render(request, 'csxii.html',context)

def hindixi(request):
    onetask= TaskList.objects.filter(subject_name='Hindi') & TaskList.objects.filter(Class_name='XI')    
    context= {'csxii':'Class-XII Topics ','alltask':onetask}
    return render(request, 'csxii.html',context)

def hindixii(request):
    onetask= TaskList.objects.filter(subject_name="Hindi")
    context= {'csxii':'Class-XII Topics ','alltask':onetask}
    return render(request, 'csxii.html',context)

def engxii(request):
    onetask= TaskList.objects.filter(subject_name="English")
    context= {'csxii':'Class-XII Topics ','alltask':onetask}
    return render(request, 'csxii.html',context)

def mathxii(request):
    onetask= TaskList.objects.filter(subject_name="Mathematics")
    context= {'csxii':'Class-XII Topics ','alltask':onetask}
    return render(request, 'csxii.html',context)



def phyxii(request):
    onetask= TaskList.objects.filter(subject_name="Physics")
    context= {'csxii':'Class-XII Topics ','alltask':onetask}
    return render(request, 'csxii.html',context)

def chexii(request):
    onetask= TaskList.objects.filter(subject_name="Chemistry")
    context= {'csxii':'Class-XII Topics ','alltask':onetask}
    return render(request, 'csxii.html',context)

def bioxii(request):
    onetask= TaskList.objects.filter(subject_name="Biology")
    context= {'csxii':'Class-XII Topics ','alltask':onetask}
    return render(request, 'csxii.html',context)


def primary(request):
    context= {'primary':'Welcome to Primary Classes e-Learning '}
    return render(request, 'primary.html',context)

def index(request):
    context= {'index':'Welcome to KV Pathshaala '}
    return render(request, 'index.html',context)


def secondary(request):
    context= {'secondary':'Welcome to Secondary Classes e-Learning'}
    return render(request, 'secondary.html',context)


def srsec(request):
    context= {'srsec':'Welcome to Senior Secondary Classes e-Learning'}
    return render(request, 'srsec.html',context)