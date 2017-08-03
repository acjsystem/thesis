# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserForm

# Create your views here.

def index(request):
	return render(request, 'carsys/index.html', {'log_stat': 'index'})

#def index(request):
	#return render(request, 'acjvone/index.html')

#def index(request):
#	return render(request, 'acjvone/index.html')

def signup(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Album.objects.filter(user=request.user)
                return render(request, 'carsys/index.html', {'log_stat': 'logged in'})
    context = {
        "form": form,
    }
    return render(request, 'carsys/signup.html', context)