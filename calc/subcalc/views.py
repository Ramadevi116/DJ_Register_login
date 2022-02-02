from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def registerpage(request):
    form=CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account was created for ' + user)
            return redirect('loginpage')
    context={'form':form}
    return render(request,'register.html',context)
def loginpage(request):

    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context={}
    return render(request, 'login.html', context)
def logout(request):
    logout(request)
    return redirect('login')


def calc(request):
    return render(request,'calc.html')
def home(request):
    Additions=Addition.objects.all()
    return render(request,'home.html',{'home':Additions})
def add(request):
    return render(request,'calc.html')
def sub(request):
    return render(request,'calc1.html')
def mul(request):
    return render(request,'calc2.html')
def div(request):
    return render(request,'calc3.html')
def options(request):
    return render(request,'option.html')
