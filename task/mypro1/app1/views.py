from django.shortcuts import render
from app1.models import*
from app1.form import*


# Create your views here.
def base(request):
    return render(request,'base.html')
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')

from app1.models import*
def base(request):
    d=student.objects.all()
    return render(request,'home.html',{'s':d})
def form1(request):
    form=studentform()
    if request.method=='POST':
        form=studentform(request.POST)
        if form.is_valid():
            form.save()
            return base(request)
    return render(request,'form1.html',{'form':form})