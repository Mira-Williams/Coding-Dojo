from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt

from .models import *

def index(request):
    return render(request, 'index.html')

def register(request):
    errors = User.objects.validate(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt()).decode()
        User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=hashed_pw,
            )
        return redirect('/success')

def login(request):
    results = User.objects.filter(email=request.POST['email'])

    if len(results) > 0:
        if bcrypt.checkpw(request.POST['password'].encode(), results[0].password.encode()):
            request.session['userid'] = results[0].id
            return redirect('/success')
        else:
            messages.error(request, "Incorrect password")
            return redirect("/")
    else:
        messages.error(request, "This email has not been registered")
        return redirect("/")
    # else:
    #     messages.error(request, "Must login first")
    #     return redirect("/")

def success(request):
    if 'userid' in request.session:
        return render(request, 'success.html')
    else:
        messages.error(request, "Must login first")
        return redirect("/")

def logout(request):
    request.session.flush()
    messages.success(request, "Logged out")
    return redirect('/')