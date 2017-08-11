from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'carsys'

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^signup/$', views.Signup.as_view(), name='signup'),
    url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^logout/$', views.Logout.as_view(), name='logout'),
]