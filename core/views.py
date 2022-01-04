from django.shortcuts import render
from .forms import StudentForm
from .models import User
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'core/home.html')
def contact_page(request):
    if request.method=="POST":
        fm=StudentForm(request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['name']
            uemail=fm.cleaned_data['email']
            upass=fm.cleaned_data['password']
            reg=User(name=uname,email=uemail,password=upass)
            messages.success(request,"data save successfully!!!")
            reg.save()
            fm=StudentForm()
    else:
        fm=StudentForm()
    return render(request,'core/contact.html',{'form':fm})
