# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(User):
	address = models.CharField(max_length=100)
	license_id = models.CharField(max_length=100)
	#check whether field can have INTEGER instead of CHAR
	contact_no = models.CharField(max_length=250)
	def __str__(self):
		return self.first_name + ' ' + self.last_name

class Car(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	plate_no = models.CharField(max_length=100)
	car_model = models.CharField(max_length=100)
	#true if stolen/carjacked false if not
	#on first car_stat true, send location
	car_stat = models.BooleanField(default=False)

	def __str__(self):
		return self.plate_no

class Report(models.Model):
	#we'll call all user info then get the user license ID to report
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
	#this column is for card ignition true for carstop false for not
	car_ignition = models.BooleanField(default=False)
	#taser can never be activated again unless there is change in report status
	taser_stat = models.BooleanField(default=False)
	#has the incident been reported or not?
	report_stat = models.BooleanField(default=False) 
	#this will show whether it was turned on or eventually turned off
	date_reported = models.DateTimeField(auto_now=True)
	#this is the location of the car
	car_loc = models.CharField(max_length=100)
	#when was location added?
	#car_loc_date = models.DateTimeField(auto_now_add=True)
  	#this is the probable thief of the car
  	#use reports.rep_person.url
	rep_photo = models.FileField()
	#when was photo added?
	#car_photo_date = models.DateTimeField(auto_now_add=True)
	#does user want location?
	car_loc_stat = models.BooleanField(default=False)
	#does user want photo?	
	car_photo_stat = models.BooleanField(default=False)
