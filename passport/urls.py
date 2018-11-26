"""passport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from passp import views

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'index/', views.signin, name='index'), 
    path(r'signout/', views.signout, name='signout'),
    path(r'form/', views.form, name='form'),
    path(r'register/', views.register, name='register'),
    path(r'wait/', views.wait, name='wait')
]
