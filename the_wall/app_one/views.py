from django.shortcuts import render, redirect
import bcrypt
from django.contrib import messages
from .models import *
import datetime

def log_n_reg(request):
    return render(request, 'log_n_reg.html')

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
    
def the_wall(request):
    if 'login_id' in request.session:
        context={
            'posts': Post.objects.all(),
            'login_id': request.session['login_id']
        }
        return render(request, 'the_wall.html', context)
    else:
        messages.error(request, 'Must login first')
        return redirect('/')

def login(request):
    user_match = User.objects.filter(email=request.POST['email'])

    if len(user_match) > 0:
        if bcrypt.checkpw(request.POST['password'].encode(), user_match[0].password.encode()):
            request.session['login_id'] = user_match[0].id
            request.session['login_first_name'] = user_match[0].first_name
            return redirect('/the_wall')
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

def process_post(request):
    Post.objects.create(
        content = request.POST['post'],
        user = User.objects.get(id=request.session['login_id'])
    )
    return redirect('/the_wall')

def add_like(request, id):
    post = Post.objects.get(id=id)
    user = User.objects.get(id=request.session['login_id'])

    if len(post.likes.filter(first_name=user.first_name)) == 0:
        post.likes.add(user)
        post.dislikes.remove(user)
    else:
        post.likes.remove(user)

    return redirect('/the_wall')

def add_dislike(request, id):
    post = Post.objects.get(id=id)
    user = User.objects.get(id=request.session['login_id'])

    if len(post.dislikes.filter(first_name=user.first_name)) == 0:
        post.dislikes.add(user)
        post.likes.remove(user)
    else:
        post.dislikes.remove(user)

    return redirect('/the_wall')

def add_comment(request, id):
    Comment.objects.create(
        content = request.POST['comment'],
        user = User.objects.get(id=request.session['login_id']),
        post = Post.objects.get(id=id)
    )
    return redirect('/the_wall')

def add_comment_like(request, id):
    comment = Comment.objects.get(id=id)
    user = User.objects.get(id=request.session['login_id'])

    if len(comment.likes.filter(id=user.id)) == 0:
        comment.likes.add(user)
        comment.dislikes.remove(user)
    else:
        comment.likes.remove(user)

    return redirect('/the_wall')

def add_comment_dislike(request, id):
    comment = Comment.objects.get(id=id)
    user = User.objects.get(id=request.session['login_id'])

    if len(comment.dislikes.filter(first_name=user.first_name)) == 0:
        comment.dislikes.add(user)
        comment.likes.remove(user)
    else:
        comment.dislikes.remove(user)

    return redirect('/the_wall')

def delete_post(request, id):
    post = Post.objects.get(id=id)
    time_diff = post.compare_time

    if post.user.id == request.session['login_id'] and time_diff < 30:
        post.delete()
        return redirect('/the_wall')
    else:
        return redirect('/the_wall')

def delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    time_diff = comment.compare_time

    if comment.user.id == request.session['login_id'] and time_diff < 30:
        comment.delete()
        return redirect('/the_wall')
    else:
        return redirect('/the_wall')
