"""Hotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from django.contrib import admin
from django.conf.urls import url , include 
from django.urls import path 
from .views import home , galeries ,services , rooms 
from rooms.views import room_list_view , room_detail_view , booking_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path( '' , home , name='home'),
    path( 'galeries/' , galeries , name='galeries'), 
    path( 'services/' , services , name='services'), 
#   path('rooms/', rooms , name='rooms'),
    path ( 'accounts/',include('accounts.urls')),
    path('rooms/', room_list_view , name='rooms'),
    path('rooms/<int:id>/', room_detail_view, name='room-detail'),
    path('rooms/<int:id>/booking/', booking_create , name='booking'),
    


    

    
]
urlpatterns += staticfiles_urlpatterns()