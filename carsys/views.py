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

# Create your views here.

def index(request):
	return render(request, 'carsys/index.html', {'log_stat': 'index'})

#def index(request):
	#return render(request, 'acjvone/index.html')

#def index(request):
#	return render(request, 'acjvone/index.html')

class Index(View):
    template_name = 'carsys/index.html'
    
    
    def get(self, request,):
      if request.user.is_authenticated():
        return render(request, self.template_name,)
      return render(request, self.template_name,)
 
class Logout(View):      
  def get(self, request):
      logout(request)
      return redirect('/login')

class Signup(View):
    template_name = 'carsys/signup.html'
    
    def get(self, request,):
      context = {}
      context['led'] = True
      context['user_data'] = 'asdasdas'
      return render(request, self.template_name, context)
    
    def post(self, request,):
      username = request.POST.get('username')
      pwd = request.POST.get('password')
      f_name = request.POST.get('f_name')
      l_name = request.POST.get('l_name')
      add = request.POST.get('address')
      lic_ID = request.POST.get('lic_ID')
      cont_no = request.POST.get('cont_no')
      
      profile = Profile()
      profile.username=username
      profile.set_password(pwd)
      profile.first_name=f_name
      profile.last_name=l_name
      profile.address=add
      profile.license_id=lic_ID
      profile.contact_no=cont_no
      profile.save()
      
      context={}
      context['username'] = username
      context['pwd'] = pwd      
      return render(request, self.template_name, context)

class Login(View):
  template_name = 'carsys/login.html'
    
  def get(self, request,):
      context = {}
      context['led'] = True
      context['user_data'] = 'asdasdas'
      return render(request, self.template_name, context)
    
  def post(self, request,):
      username = request.POST.get('username')
      pwd = request.POST.get('password')
      
      user = authenticate(username=username, password=pwd)
      print user, "DSADASDSA"
      if user is not None:
        print "success"
        return render(request, self.template_name)
      else:
        print "Fail", "dssdfds"
        return render(request, self.template_name,)
      




