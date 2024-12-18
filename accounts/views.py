from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth import logout
from . models import *
from django.contrib.auth import login,authenticate
from . forms import *
from django.contrib.auth.decorators import login_required
def custom_logout(request):
    logout(request)  
    return redirect('/accounts/login/') 
def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save() 
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=password)
            login(request, user)
            return redirect('/product/')
    else:
        form= UserCreationForm()
    context={'form':form}
    return render(request,'registration/signup.html',context)     

@login_required(login_url='/accounts/login/')  
def profile(request,slug):
    profile=get_object_or_404(Profile,slug=slug)
    context={'profile':profile}

    return render(request,'registration/profile.html',context)       

