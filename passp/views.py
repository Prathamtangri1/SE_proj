# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *
import random
import datetime
import string

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

@csrf_exempt
def signin(request):
    if request.user.is_authenticated and request.user.is_active == True :
        return redirect('form')
    if request.method == 'POST':
        aadhar_no = request.POST['aadhar_no']
        try:
            user = User._default_manager.get(username__iexact = aadhar_no.lower())
            print(user)
            username = user.username
        except:
            print("username invalid")
            return render(request, 'pass/index.html', {'error' : 'User-Name/Password Invalid'})
        password = request.POST['password']
        print(username)
        user = authenticate(username = username, password = password)
        if user == None :
            return render(request, 'pass/index.html', {'error' : 'User-Name/Password Invalid'})
        elif user.is_active == False :
            login(request, user)
            return redirect('form')
        else : 
            login(request, user)
            return redirect('form')
    return render(request, 'pass/index.html', None)

@csrf_exempt
def signout(request):
    logout(request)
    return redirect('index')

@csrf_exempt
def form(request):
    if request.method == 'POST':
        name = request.POST['name']
        father_name = request.POST['father_name']
        dob = request.POST['dob']
        current_add = request.POST['current_add']
        permanent_add = request.POST['permanent_add']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email = request.POST['email']
        passport_number = id_generator()
        pass_ = Passport(passport_number=passport_number, name=name, father_name=father_name, dob=dob, current_add=current_add, permanent_add=permanent_add, gender=gender, phone=phone, email=email)
        if pass_ == None :
            return render('pass/fill_form.html', {'error' : "Authentication Error, Please Try Again."})
        pass_.save()
        request.user.is_active = True
        #request.user.save()
        return redirect('wait')
    return render(request, 'pass/fill_form.html', None)

@csrf_exempt
def register(request):
    if request.user.is_active == True:
        return redirect('form')
    if request.method == 'POST':
        username = request.POST['aadhar']
        passwd = request.POST['password1']
        passwd2 = request.POST['password2']
        if(passwd != passwd2):
            return render(request, 'pass/register.html', {'error' : 'Passwords don\'t match'})
        try:
            user = User._default_manager.get(username__iexact = username.lower())
            return render(request, 'pass/register.html', {'error':'User-Name Already Exists'})
        except User.DoesNotExist:
            user = User.objects.create_user(username = username)
            user.set_password(passwd)
            user.save()
            profile = Applicant()
            profile.user = user
            profile.status = 'no'
            profile.ministry = 'N'
            profile.police = 'N'
            profile.dispatch = 'N'
            profile.date = 'N'
            profile.save()
            user = authenticate(username=username, password=passwd)
            login(request, user)
        
        return redirect('index')
    return render(request, 'pass/register.html', None)

@csrf_exempt
def wait(request):
    if(not request.user.is_active):
        return redirect('index')

    profile = Applicant.objects.get(user=request.user)
    if(request.method == "POST"):
        profile.date = str(request.POST['date'])
        profile.save()
        return render(request, 'pass/status2.html', {'status' : profile.status, 'date' : profile.date, 'ministry' : profile.ministry, 'police' : profile.police, 'dispatch' : profile.dispatch})
    return render(request, 'pass/status2.html', {'status' : profile.status, 'date' : profile.date, 'ministry' : profile.ministry, 'police' : profile.police, 'dispatch' : profile.dispatch})
