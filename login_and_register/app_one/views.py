from django.shortcuts import render, redirect
import bcrypt
from django.contrib import messages
from .models import *

def index(request):
    return render(request, 'index.html')

def register(request):
    errors = User.objects.validate(request.POST)

    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')    

    else:
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()

        User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = hashed_pw,
        )
        messages.success(request, 'User account created')
        return redirect('/')
    
def success(request):
    if 'login_id' in request.session:
        current_user = User.objects.get(id=request.session['login_id'])
        context={
            'name' : current_user.first_name + ' ' + current_user.last_name
        }
        return render(request, 'success.html', context)
    else:
        messages.error(request, 'Must login first')
        return redirect('/')

def login(request):
    user_match = User.objects.filter(email=request.POST['email'])

    if len(user_match) > 0:
        if bcrypt.checkpw(request.POST['password'].encode(), user_match[0].password.encode()):
            request.session['login_id'] = user_match[0].id
            return redirect('/success')
        else:
            messages.error(request, 'Incorrect password')
            return redirect('/')
    else:
        messages.error(request, 'Email not registered')
        return redirect('/')

def logout(request):
    request.session.flush()
    messages.success(request, 'User logged out')
    return redirect('/')