from django.shortcuts import render

# Create your views here.
from app.models import *
from app.form import *


def home(request):
    return render(request,'base.html')

def upload(request):
    form=bookform()
    if(request.method=="POST"):
        form=bookform(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return home(request)
    return render(request,'add.html',{'form':form})

def booklist(request):
    b=Book.objects.all()
    return render(request,'list.html',{'b':b})