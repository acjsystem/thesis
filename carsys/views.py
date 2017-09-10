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
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
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

class CarPhoto(APIView):
  
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
      if Report.objects.filter(car_id=car_id).exclude(car_loc="").exists():
        """if not Report.objects.filter(car_id=car_id).exclude(rep_photo="").order_by('-date_reported')[0].exists():
          report0=""
          date0=""
        else:"""
        try:
          report0=Report.objects.filter(car_id=car_id).exclude(rep_photo="").order_by('-date_reported')[0].rep_photo
          date0=Report.objects.filter(car_id=car_id).exclude(rep_photo="").order_by('-date_reported')[0].date_reported
        except IndexError:
          report0=""
          date0=""
        
        try:
          report1=Report.objects.filter(car_id=car_id).exclude(rep_photo="").order_by('-date_reported')[1].rep_photo
          date1=Report.objects.filter(car_id=car_id).exclude(rep_photo="").order_by('-date_reported')[1].date_reported
        except IndexError:
          report1=""
          date1=""
         
        try:
          report2=Report.objects.filter(car_id=car_id).exclude(rep_photo="").order_by('-date_reported')[2].rep_photo
          date2=Report.objects.filter(car_id=car_id).exclude(rep_photo="").order_by('-date_reported')[2].date_reported
        except IndexError:
          report2=""
          date2=""
        
        try:
          report3=Report.objects.filter(car_id=car_id).exclude(rep_photo="").order_by('-date_reported')[3].rep_photo
          date3=Report.objects.filter(car_id=car_id).exclude(rep_photo="").order_by('-date_reported')[3].date_reported
        except IndexError:
          report3=""
          date3=""
        

        try:
          report4=Report.objects.filter(car_id=car_id).exclude(rep_photo="").order_by('-date_reported')[4].rep_photo
          date4=Report.objects.filter(car_id=car_id).exclude(rep_photo="").order_by('-date_reported')[4].date_reported
        except IndexError:
          report4=""
          date4=""

        
        print ('status is true')
        data = {}
        data['report0']=str(report0)
        data['date0']=str(date0)
        data['report1']=str(report1)
        data['date1']=str(date1)
        data['report2']=str(report2)
        data['date2']=str(date2)
        data['report3']=str(report3)
        data['date3']=str(date3)
        data['report4']=str(report4)
        data['date4']=str(date4)
        data['Error']="False"

        return Response(data,)
      else:          
        data = {}
        data['car']=str(car)
        data['status']="No reports"
        data['Error']="True"
        return Response(data,)
    else:
      data = {}
      data['car']=str(car)
      data['car_stat']=str(car_stat)
      data['status']="No car"
      data['Error']="False"
      return Response(data,)
    return Response({'Error':'True'}, status=status.HTTP_400_BAD_REQUEST)

class CarLocations(APIView):
  #returns 10 locations
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
        if Report.objects.filter(car_id=car_id).exclude(car_loc="").exists():
          #report=Report.objects.filter(car_id=car_id).exclude(rep_photo="").order_by('-date_reported')
          report=Report.objects.filter(car_id=car_id).exclude(car_loc="").order_by('-date_reported')
          
          data = serializers.serialize('json', report)
          struct = json.loads(data)
          data = json.dumps(struct)
          return Response(data,)
        else:          
          data = {}
          data['car']=str(car)
          data['status']="No reports"
          data['Error']="True"
          return Response(data,)
      else:
        data = {}
        data['car']=str(car)
        data['car_stat']=str(car_stat)
        data['Error']="False"
        return Response(data,)
    return Response({'Error':'True'}, status=status.HTTP_400_BAD_REQUEST)






class CarLocation(APIView):
  
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
        if Report.objects.filter(car_id=car_id).exclude(car_loc="").exclude(car_loc="Location Not Fixed.").exists():
          report=Report.objects.filter(car_id=car_id).exclude(car_loc="").exclude(car_loc="Location Not Fixed.").order_by('-date_reported')[0]
          user = report.user.id
          car_id = report.car_id.id
          car_loc = report.car_loc
          date_reported=report.date_reported
          print ('status is true')
          data = {}
          data['car']=str(car)
          data['user']=str(user)
          data['car_id']=str(car_id)
          data['car_loc']=str(car_loc)
          data['date_reported']=str(date_reported)
          data['Error']="False"
          return Response(data,)
        else:          
          data = {}
          data['car']=str(car)
          data['status']="No location"
          data['Error']="True"
          return Response(data,)
      else:
        data = {}
        data['car']=str(car)
        data['car_stat']=str(car_stat)
        data['Error']="False"
        return Response(data,)
    return Response({'Error':'True'}, status=status.HTTP_400_BAD_REQUEST)





#List all users or create
class ProfileList(APIView):
  #getting all users
  def get(self,request):
    user = Profile.objects.all()
    serializer = ProfileSerializer(user, many=True)
    return Response(serializer.data)

  def post(self,request):
    #this is for adding new user
    username = request.data['username']
    pwd = request.data['password']
    last_name = request.data['last_name']
    first_name = request.data['first_name']
    #saves user info
    profile = Profile()
    profile.username = username
    profile.set_password(pwd)
    profile.first_name = first_name
    profile.last_name = last_name
    profile.address = request.data['address']
    profile.license_id = request.data['license_id']
    profile.contact_no = request.data['contact_no']

    #does the username exist
    if User.objects.filter(username=username).exists():
      print ('rejected')
      data = {
      'Error': 'Username is taken'
      }     
      return Response(data,)
    elif User.objects.filter(last_name=last_name,first_name=first_name).exists():
      print('rejected')
      data = {
      'Error':'User already exists!'
      }
      return Response(data,)
    else:        
      print ('added')
      profile.save()

      data = {
      'Success': "User added.",
      }
      return Response(data,)
    return Response(data,)

class UserDetail(APIView):
  #getting all users
  def get(self,request):
    user = Profile.objects.all()
    serializer = ProfileSerializer(user, many=True)
    return Response(serializer.data)

  def post(self,request):
    #update user info
    username = request.data['username']
    pwd = request.data['password']
    last_name = request.data['last_name']
    first_name = request.data['first_name']
    #saves user info

    #does the username exist
    if User.objects.filter(username=username).exists():
      user = authenticate(request, username=username, password=pwd)
      if user is not None:
        profile = Profile.objects.filter(username=username)[0]
        print ('accepted')
        profile.username = username
        profile.set_password(pwd)
        profile.first_name = first_name
        profile.last_name = last_name
        profile.email = request.data['email']
        profile.license_id = request.data['license_id']
        profile.contact_no = request.data['contact_no']
        profile.save()
        data = {
        'Success': 'Changes were saved!'
        }     
        return Response(data,)
      else:
        data = {
        'Error': 'Incorrect Password!'
        }     
        return Response(data,)

    else:        
      print ('rejected')
      data = {
      'Error': "User doesn't exist!",
      }
      return Response(data,)
    return Response(data,)



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
    #user = Car.objects.all()
    #serializer = CarSerializer(user, many=True)
    data = {}
    data['Carlist'] = "Add car"
    return Response(data)

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
        data['Error'] = "False"
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
      car_id=car.id
      if car_stat == "True":
        car.car_stat = True
        car.save()
      else:
        car.car_stat = False
        rep = Report()
        rep.user=user
        rep.car_id = car
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
    serializer = ReportSerializer(data=request.data)#,files=request.files
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
    
    if user is not None:
      login(request, user)
      print (request.user.is_authenticated())
      if request.user.is_authenticated():
        data = {}
        data['user'] = "logined"
        
        user_num = User.objects.filter(username = username)
        u_num = user_num[0].id
        if Car.objects.filter(user = u_num).exists():
          car = Car.objects.filter(user = u_num)[0]
          car_stat = car.car_stat
          car_plate = car.plate_no
          car_id = car.id
          if Report.objects.filter(car_id=car_id,car_loc="",rep_photo= "").exists():
            report = Report.objects.filter(car_id=car_id,car_loc="",rep_photo= "").order_by('-date_reported')[0]
            ignition = report.car_ignition
            taser = report.taser_stat
            car_loc_stat = report.car_loc_stat
            car_photo_stat = report.car_photo_stat

            data['ignition'] = str(ignition)
            data['taser'] = str(taser)
            data['loc_stat'] = str(car_loc_stat)
            data['photo_stat'] = str(car_photo_stat)
          else:
            data['ignition'] = "False"
            data['taser'] = "False"
            data['loc_stat'] = "False"
            data['photo_stat'] = "False"
          
          data['car_stat'] = car_stat
          data['car_plate'] = car_plate
        else:
          data['car_stat'] = "0"
          data['car_plate'] = "0"
          
        return Response(data,)
      #return redirect('/proflist')
    else:
      return Response({"user":"invalid login"},)

class UserData(APIView):
  def get(self,request):
    data={'acjcarsystem':'RPi gets user number'}
    return Response(data)

  def post(self, request,):
    #tget car num
    plate_no = request.data['plate_no']
    if Car.objects.filter(plate_no=plate_no).exists():
      car = Car.objects.get(plate_no=plate_no)
      user = car.user
      car_id = car.id
      car=car.plate_no
      cont_no=Profile.objects.get(username=user).contact_no
      print ('found car')      
      print (user)      
      data = {}
      data['car']=str(car)
      data['car_id']=str(car_id)
      data['username']=str(user)
      data['cont_no']=str(cont_no)
      return Response(data,)
    return Response({'ERROR':'CAR0'}, status=status.HTTP_400_BAD_REQUEST)
  
class UserInfo(APIView):
  def get(self,request):
    data={'acjcarsystem':'Phone gets user info'}
    return Response(data)

  def post(self, request,):
    #tget car num
    username = request.data['username']
    if Profile.objects.filter(username=username).exists():
      prof = Profile.objects.filter(username=username)[0]
      f_name = prof.first_name
      l_name = prof.last_name
      email = prof.email
      contact_no = prof.contact_no
      license_id = prof.license_id
      
      print ('userinfo')      
      print (username)      
      data = {}
      data['f_name']=str(f_name)
      data['l_name']=str(l_name)
      data['email']=str(email)
      data['contact_no']=str(contact_no)
      data['license_id']=str(license_id)
      data['Error']="False"
      return Response(data,)
    return Response({'Error':'No user found'}, status=status.HTTP_400_BAD_REQUEST)



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
            report = Report.objects.filter(car_id=qcar,car_loc="",rep_photo="").order_by('-date_reported')[0]
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
