from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse 
from .forms import *


def home(request):
    if(str(request.user)!="AnonymousUser"):
        if request.method == 'POST': 
            form = PicForm(request.POST, request.FILES)

            if form.is_valid(): 
                form.save() 
                # messages.success(request, ('Image Successfully Uploaded!')) 
                return redirect('home')
        else: 
            form = PicForm() 
            gals = Gallery.objects.order_by('-uploaded')[3:]
            gals_top = Gallery.objects.order_by('-uploaded')[:3]
        context = {'form': form, 'gal_imges_top': gals_top, 'gal_imges_rem': gals}
        return render(request, 'gals/homein.html', context)
    else:
        return render(request, 'gals/home.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, ('Logged in!'))
            return redirect('home')
        else:
            # messages.success(request, ('Error Logging in!'))
            return redirect('login')
    else:
        return render(request, 'gals/login.html', {})

def logout_user(request):
    logout(request)
    # messages.success(request, ('Logged out!'))
    return redirect('home')

def reg_user(request):
    if request.method == 'POST':
        form = SignUpForms(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            # messages.success(request, ('Registered!'))
            return redirect('login')

    else:
        form = SignUpForms()

    context = {'form': form}
    return render(request, 'gals/register.html', context)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForms(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            # messages.success(request, ('Profile Updated!'))
            return redirect('home')

    else:
        form = EditProfileForms(instance=request.user)

    context = {'form': form}
    return render(request, 'gals/edit_profile.html', context)

def change_password(request):
    if request.method == 'POST':
        form = EditPassForms(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            # messages.success(request, ('Password Updated!'))
            return redirect('home')

    else:
        form = EditPassForms(user=request.user)

    context = {'form': form}
    return render(request, 'gals/change_password.html', context)