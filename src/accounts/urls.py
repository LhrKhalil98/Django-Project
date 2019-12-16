from django.conf.urls import url 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from django.urls import path 
from .views import  signup_view , login_view ,logout_view

app_name='accounts'

urlpatterns=[
    path('signup1/',signup_view , name='signup'), 
    path('login/',login_view , name='login'),
    path('logout/',logout_view , name='logout'),

]