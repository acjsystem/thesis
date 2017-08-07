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
# Register your models here.
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Car)
admin.site.register(Reports)
