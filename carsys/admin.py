# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = (
            'id',
            'username',
            'first_name',
            'address',
            'license_id',
            'contact_no',
            )
    list_filter = (
            'id',
            'username',
            'first_name',
            'address',
            'license_id',
            'contact_no',
           )
    search_fields = (
            )
    readonly_fields = (
            )

class ReportAdmin(admin.ModelAdmin):
    list_display = (
            'user',
            'car_ignition',
            'taser_stat',
            'report_stat',
            'date_reported',
            'car_loc',
            )
    list_filter = ('date_reported', 'user',
           )
    search_fields = (
            )
    readonly_fields = ('date_reported',
            )
# Register your models here.
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Car)

admin.site.register(Report, ReportAdmin)
