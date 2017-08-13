# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserForm
from django.views.generic import View
from django.http import JsonResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.models import User
from datetime import datetime

# Create your views here.


class Index(View):
    template_name = 'carsys/index.html'    
    
    def get(self, request,):
      #signup = request.session.pop('signup', False)
      if request.user.is_authenticated():
        q = Car.objects.filter(user=request.user)
        selected_car = request.POST.get('car')
        context = {
        'user_data': request.user.username,
        'q': q,
        'selected_car': selected_car,
        }
        return render(request, self.template_name, context)
      else:
        context = {
          'error_message': 'You need to log in first!',
          }
        return render(request, 'carsys/login.html', context)
    def post(self, request,):      
      if request.user.is_authenticated():
          q = Car.objects.filter(user=request.user)
          selected_car = request.POST.get('car')
          qcar = Car.objects.filter(plate_no=selected_car)[0]
          if not Report.objects.filter(car_id=qcar):
            report='here'
          else:
            report = Report.objects.filter(car_id=qcar)[0]
          context = {
          'user_data': request.user.username,
          'q': q,
          'selected_car': qcar,
          'report': report,
          }
          print ("success")
          return render(request, self.template_name, context)

class Caron(View):      
  def post(self, request,):      
      if request.user.is_authenticated():          
          selected_car = request.POST.get('selcar')
          qcar = Car.objects.filter(plate_no=selected_car)[0]
          qcar.car_stat = True
          qcar.save()          
          print ("success car on")
          return redirect('/')

class Caroff(View):      
  def post(self, request,):      
      if request.user.is_authenticated():          
          selected_car = request.POST.get('selcar')
          qcar = Car.objects.filter(plate_no=selected_car)[0]
          rep=Report()
          #turn car off
          if request.POST.get('carstem'):
            qcar.car_stat = request.POST.get('carstem')
            rep.user=Car.objects.filter(plate_no=selected_car)[0].user
            rep.car_id = qcar
            rep.car_ignition = False;
            rep.taser_stat = False;
            rep.report_stat = False;
            rep.car_loc_stat = False;
            rep.date_reported = datetime.now();
            rep.car_photo_stat = False;
          else:
            qcar.car_stat = True;
            rep.user=Car.objects.filter(plate_no=selected_car)[0].user
            rep.car_id = qcar
            rep.date_reported = datetime.now();
            if request.POST.get('ignition'):
              rep.car_ignition=request.POST.get('ignition')
            else:
              rep.car_ignition = False;
            if request.POST.get('taser'):
              rep.taser_stat=request.POST.get('taser')
            else:
              rep.taser_stat = False;
            if request.POST.get('report'):
              rep.report_stat=request.POST.get('report')
            else:
              rep.report_stat = False;
            if request.POST.get('location'):
              rep.car_loc_stat=request.POST.get('location')
            else:
              rep.car_loc_stat = False;
            if request.POST.get('photo'):
              rep.car_photo_stat=request.POST.get('photo')  
            else:
              rep.car_photo_stat = False;
          rep.save()
          qcar.save()          
          #report table
          
          
          print ("success car updates")
          return redirect('/')

class AddCar(View):
    template_name = 'carsys/add_car.html'    
    
    def get(self, request,):
      #signup = request.session.pop('signup', False)
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
        car=Car()
        car.user = request.user
        plate_no = request.POST.get('plate_no')      
        car.plate_no=plate_no
        car.car_model=request.POST.get('car_mo')
        car.car_stat=False
        #does the username exist
        if Car.objects.filter(plate_no=plate_no).exists():
          print ('rejected')
          context = {
          'error_message': 'That car is already added!',
          }     
          return render(request, self.template_name, context) 
        else:        
          print ('caradded')
          car.save()
          return redirect('/')
      else:
        context = {
          'error_message': 'You need to log in first!',
          'key2': 'world',
          }
        return render(request, 'carsys/login.html', context)

class Logout(View):      
  def get(self, request):
      logout(request)
      request.session['signup'] = False
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
      
      username = request.POST.get('username')
      pwd = request.POST.get('password')
      #saves user info
      profile = Profile()
      profile.username=username
      profile.set_password(pwd)
      profile.first_name=request.POST.get('f_name')
      profile.last_name=request.POST.get('l_name')
      profile.address=request.POST.get('address')
      profile.license_id=request.POST.get('lic_ID')
      profile.contact_no=request.POST.get('cont_no')

      #does the username exist
      if User.objects.filter(username=username).exists():
        print ('rejected')
        context = {
        'error_message': 'Username is taken',
        'key2': 'world',
        }     
        return render(request, self.template_name, context) 
      else:        
        print ('added')
        profile.save()
        user = authenticate(request, username=username, password=pwd)
        login(request, user)
        request.session['signup'] = True
        
        context = {
        'user_data': username,
        'led': 'on',
        }
        return redirect('/')

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
          print ("success")
          return redirect('/')
        else:
          context = {
          'error_message': 'Invalid Username/Password',
          'key2': 'world',
          }
          print ("Fail")
          return render(request, self.template_name, context)
      

