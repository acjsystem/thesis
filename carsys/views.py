# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import status,generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import *
from .forms import UserForm
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, JsonResponse
from datetime import datetime
import json


"""
START OF DJANGO REST
"""
# Create your views here.
#List all users or create
class ProfileList(APIView):
  #getting all users
  def get(self,request):
    user = Profile.objects.all()
    serializer = ProfileSerializer(user, many=True)
    return Response(serializer.data)

  def post(self,request):
    #this is for adding new user
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class ProfileDetail(APIView):
  def get(self,request):
    #this is for getting of user data
    data={'acjcarsystem':'Phone updates car status'}
    return Response(data)

  def post(self,request):
    #this is for update of user data
    data = {}
    data['Error']="True"
    #user = request.data['user']
    plate_no = request.data['plate_no']
    car_stat = request.data['car_stat']
    if Car.objects.filter(plate_no=plate_no).exists():
      car = Car.objects.filter(plate_no=plate_no)[0]
      car.car_stat = car_stat
      car.save()
      data['Error']="False"
      data['user']=str(car.user)
      data['plate_no']=str(car.plate_no)
      data['car_stat']=str(car.car_stat)
      return Response(data,)
    data['error_message']="No car found."
    return Response(data, status=status.HTTP_400_BAD_REQUEST)
 
class CarList(APIView):
  def get(self,request):
    user = Car.objects.all()
    serializer = CarSerializer(user, many=True)
    return Response(serializer.data)

  def post(self,request):    
    #add car
    user = request.data['user']
    plate_no = request.data['plate_no']
    car_model = request.data['car_model']
    if User.objects.filter(username=user).exists():
      user = User.objects.filter(username=user)[0]
      car = Car()
      car.user = user
      car.plate_no = plate_no
      car.car_model = car_model
      car.car_stat = False
      #does the username exist
      if Car.objects.filter(plate_no=plate_no).exists():
        print ('rejected')
        return Response({'Error':'Car already exists'}, status=status.HTTP_400_BAD_REQUEST) 
      else:        
        print ('caradded')
        car.save()
        data = {}
        data['user'] = str(car.user)
        data['plate_no'] = str(car.plate_no)
        data['car_model'] = str(car.car_model)
        data['car_stat'] = str(car.car_stat)
        return Response(data,)
    else:
      return Response({'Error':'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)
class ChangeCarStat(APIView):
  def get(self,request):
    data={'acjcarsystem':'RPi changes carstat'}
    return Response(data)

  def post(self,request):
    plate_no = request.data['plate_no']
    car_stat = request.data['car_stat']
    if Car.objects.filter(plate_no=plate_no).exists():
      car = Car.objects.get(plate_no=plate_no)
      user = car.user
      car_id=car.car_id
      if car_stat == "True":
        car.car_stat = True
        car.save()
      else:
        car.car_stat = False
        rep = Report()
        rep.user=user
        rep.car_id = car_id
        rep.car_ignition = False
        rep.taser_stat = False
        rep.car_loc_stat = False
        rep.car_photo_stat = False
        rep.save()
        car.save()
      data ={}
      data ['car_id'] = car_id
      data ['car_stat'] = car_stat
      data ['plate_no'] = plate_no
      data ['Error'] = "False"
      return Response(data,)
    else:
      data = {}
      data['Error']="True"
      return Response(data,)

class CarDetail(APIView):
  
  def get(self,request):
    data={'acjcarsystem':'RPi gets reports'}
    return Response(data)

  def post(self, request,):
    #this is for adding new user
    plate_no = request.data['plate_no']
    if Car.objects.filter(plate_no=plate_no).exists():
      car = Car.objects.get(plate_no=plate_no)
      car_id=car.id
      car_stat = car.car_stat
      if car_stat:
        #if Report.objects.filter(plate_no=plate_no).exists():
        report=Report.objects.filter(car_id=car_id,car_loc="",rep_photo= "").order_by('-date_reported')[0]
        user = report.user.id
        car_id = report.car_id.id
        ignition = report.car_ignition
        taser = report.taser_stat
        report_st=report.report_stat
        date_reported=report.date_reported
        car_loc_stat=report.car_loc_stat
        car_photo_stat=report.car_photo_stat
        print ('status is true')
        data = {}
        data['car']=str(car)
        data['user']=str(user)
        data['car_id']=str(car_id)
        data['car_stat']=str(car_stat)
        data['ignition']=str(ignition)
        data['taser']=str(taser)
        data['loc_stat']=str(car_loc_stat)
        data['photo_stat']=str(car_photo_stat)
        data['date_reported']=str(date_reported)
        data['Error']="False"
        return Response(data,)
      else:
        data = {}
        data['car']=str(car)
        data['car_stat']=str(car_stat)
        data['Error']="False"
        return Response(data,)
    return Response({'Error':'True'}, status=status.HTTP_400_BAD_REQUEST)

class AddReport(APIView):
  
  def get(self,request):
    data={'acjcarsystem':'RPi sends reports'}
    return Response(data)

  def post(self, request,):
    #this is for adding new user
    serializer = ReportSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class Auth(APIView):
  #getting all users
  def get(self,request):
    data={'acjcarsystem':'Login API'}
    return Response(data)

  def post(self, request,):
    #this is for adding new user
    username = request.data['username']
    pwd = request.data['password']
    user = authenticate(request, username=username, password=pwd)
    login(request, user)
    print (request.user.is_authenticated())
    if user is not None:
      if request.user.is_authenticated():
        return Response({"user":"logined"},)
      return redirect('/proflist')
    else:
      return Response({"user":"invalid login"},)

class UserData(APIView):
  def get(self,request):
    data={'acjcarsystem':'RPi gets user number'}
    return Response(data)

  def post(self, request,):
    #this is for adding new user
    plate_no = request.data['plate_no']
    if Car.objects.filter(plate_no=plate_no).exists():
      car = Car.objects.get(plate_no=plate_no)
      user = car.user
      car=car.plate_no
      cont_no=Profile.objects.get(username=user).contact_no
      #serializer = UserSerializer(car, data=request.data)
      #if serializer.is_valid():
      print ('found car')      
      print (user)      
      data = {}
      data['car']=str(car)
      data['username']=str(user)
      data['cont_no']=str(cont_no)
      return Response(data,)
    return Response({'ERROR':'CAR0'}, status=status.HTTP_400_BAD_REQUEST)

    """       
      
    username = request.data['car_no']
    pwd = request.data['password']
    user = authenticate(request, username=username, password=pwd)
    login(request, user)
    print (request.user.is_authenticated())
    if user is not None:
      if request.user.is_authenticated():
        return Response({"user":"logined"},)
      return redirect('/proflist')
    else:
      return Response({"user":"invalid login"},)
      """
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
END OF DJANGO REST
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



"""
START OF DJANGO WEB
"""
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
