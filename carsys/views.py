# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserForm
from django.views.generic import View
from django.http import JsonResponse
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.models import User

# Create your views here.


class Index(View):
    template_name = 'carsys/index.html'    
    
    def get(self, request,):
      
      if request.user.is_authenticated():
        context = {
          'user_data': request.user.username,
          'led': '-',
          }
        return render(request, self.template_name, context)
      else:
        context = {
          'error_message': 'You need to log in first!',
          'key2': 'world',
          }
        return render(request, 'carsys/login.html', context)
    def post(self, request,):
      
      if request.user.is_authenticated():
          led = request.POST.get('led')
          context = {
          'user_data': request.user.username,
          'led': led,
          }
          print "success"          
          return render(request, 'carsys/index.html', context)

class Logout(View):      
  def get(self, request):
      logout(request)
      request.session['signup'] = True
      return redirect('/login')

class Signup(View):
    template_name = 'carsys/signup.html'
    
    def get(self, request,):
      if request.user.is_authenticated():
        context = {
          'user_data': request.user.username,
          'led': 'on',
          }
        return render(request, 'carsys/index.html', context)
      context = {}
      context['led'] = True
      context['user_data'] = 'asdasdas'
      return render(request, self.template_name, context)
    
    def post(self, request,):
      if request.user.is_authenticated():
        context = {
          'user_data': request.user.username,
          'led': 'on',
          }
        return render(request, 'carsys/index.html', context)
      
      context = {
        'error_message': 'You need to log in first!',
        'key2': 'world',
        }
      return render(request, 'carsys/login.html', context)
      username = request.POST.get('username')
      #saves user info
      profile = Profile()
      profile.username=username
      profile.set_password(request.POST.get('password'))
      profile.first_name=request.POST.get('f_name')
      profile.last_name=request.POST.get('l_name')
      profile.address=request.POST.get('address')
      profile.license_id=request.POST.get('lic_ID')
      profile.contact_no=request.POST.get('cont_no')

      #does the username exists
      if User.objects.filter(username=username).exists():
        print 'rejected'
        context = {
        'error_message': 'Username is taken',
        'key2': 'world',
        }     
        return render(request, self.template_name, context) 
      else:        
        print 'added'
        profile.save()
        context = {
        'user_data': username,
        'led': 'on',
        }
        return render(request, 'carsys/index.html',context)

class Login(View):
  template_name = 'carsys/login.html'
    
  def get(self, request,):
      
      if request.user.is_authenticated():
        context = {
          'user_data': request.user.username,
          'led': 'on',
          }
        return render(request, 'carsys/index.html', context)
      context = {}
      context['led'] = True
      context['user_data'] = 'asdasdas'
      return render(request, self.template_name, context)
    
  def post(self, request,):
      signup = request.session.pop('signup', False)
      if signup:
        context = {
          'user_data': request.user.username,
          'led': 'on',
          }
        return render(request, 'carsys/index.html', context)
      else:
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request, username=username, password=pwd)
        if user is not None:
          login(request, user)
          request.session['signup'] = True
          context = {
          'user_data': username,
          'led': 'on',
          }
          print "success"          
          return redirect('/')
        else:
          context = {
          'error_message': 'Invalid Username/Password',
          'key2': 'world',
          }
          print "Fail"
          return render(request, self.template_name, context)
      




