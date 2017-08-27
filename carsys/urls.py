from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'carsys'

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^signup/$', views.Signup.as_view(), name='signup'),
    url(r'^addcar/$', views.AddCar.as_view(), name='addcar'),
    url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^logout/$', views.Logout.as_view(), name='logout'),
    url(r'^caron/$', views.Caron.as_view(), name='caron'),
    url(r'^caroff/$', views.Caroff.as_view(), name='caroff'),
    url(r'^proflist/$', views.ProfileList.as_view(), name='proflist'),
    url(r'^profdetail/$', views.ProfileDetail.as_view(), name='proflistdet'),
    url(r'^carlist/$', views.CarList.as_view(), name='carlist'),
    url(r'^cardetail/$', views.CarDetail.as_view(), name='carlistdet'),
    url(r'^auth/$', views.Auth.as_view(), name='auth'),
    url(r'^userdata/$', views.UserData.as_view(), name='userdata'),
    url(r'^addreport/$', views.AddReport.as_view(), name='addrep'),
    url(r'^changecarstat/$', views.ChangeCarStat.as_view(), name='changecarstat'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
