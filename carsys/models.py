# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# Create your models here.

class User(models.Model):
	last_name = models.CharField(max_length=100)
	first_name = models.CharField(max_length=100)
	mid_name = models.CharField(max_length=100)
	license_id = models.CharField(max_length=100)
	#check whether field can have INTEGER instead of CHAR
	contact_no = models.CharField(max_length=250)

	def __str__(self):
		return self.first_name + ' ' + self.last_name

class Car(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	plate_no = models.CharField(max_length=100)
	car_model = models.CharField(max_length=100)
	report_stat = models.BooleanField(default=False)

	def __str__(self):
		return self.plate_no

class Reports(models.Model):
	#we'll call all user info then get the user license ID to report
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
	#this will show whether it was turned on or eventually turned off
	date_reported = models.DateTimeField(auto_now_add=True)
  	#this is the location of the car
  	car_loc = models.CharField(max_length=100)
  	#this is the probable thief of the car
  	#use reports.rep_person.url
  	rep_person = models.FileField()
  