"""
URL configuration for artfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index/', views.index,name='index'),
    path('admin1/', views.admin1),
    path('artist_profile/', views.artistprofile),
    path('create_artist/', views.createartist,name='signup'),
    path('create_artist1/', views.createartist1),
    path('login_artist/', views.loginartist,name='login_artist'),
    path('login1/',views.login1),
    path('artistHome/',views.artistHome),
    path('guestHome/',views.guestHome),
    path('adminHome/',views.adminHome),
    path('addart/',views.addart),
    path('guest_login/', views.guestlogin,name='guest'),
    path('addguest/', views.addguest, name='addguest'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)