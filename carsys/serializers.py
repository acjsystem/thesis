from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = '__all__'
		extra_kwargs = {
        'address': {'required': False},
        'license_id': {'required': False},
        'contact_no': {'required': False},
    } 

class CarSerializer(serializers.ModelSerializer):
	user = ProfileSerializer()
	class Meta:
		model = Car
		fields = [
			'user',
			'plate_no',
			'car_stat'
		]

class ReportSerializer(serializers.ModelSerializer):
	#user = ProfileSerializer()
	class Meta:
		model = Report
		fields = '__all__'
		extra_kwargs = {
        'taser_stat': {'required': False},
        'report_stat': {'required': False},
        'car_ignition': {'required': False},
        'car_loc': {'required': False},
        'rep_photo': {'required': False},
        'car_loc_stat': {'required': False},
        'car_photo_stat': {'required': False},
    } 		
	 

"""
class UserLogin(serializers.ModelSerializer):
	#user = ProfileSerializer()
	#email = EmailField(label='Email Address')
	token=CharField()
	username = CharField()
	class Meta:
		model = Profile
		fields = [
			'username',
			'password',
		]		
		extra_kwargs = {"password":
							{"write_only":True}
						}
"""