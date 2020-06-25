from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'index.html', context)

def create_course(request):
    errors = Course.objects.course_validate(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
    else:
        course = Course.objects.create(
            name = request.POST['name']
        )
        desc = Description.objects.create(desc_content=request.POST['desc_content'])
        course.description = desc
        course.save()

    return redirect('/')

def comments_page(request, id):
    context = {
        'course': Course.objects.get(id=id)
    }
    return render(request, 'comments.html', context)

def create_comment(request, id):
    errors = Comment.objects.comment_validate(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
    else:
        Comment.objects.create(
            comm_content = request.POST['comm_content'],
            course = Course.objects.get(id=id)
        )
    return redirect(f'/comments/{id}')

def delete_alert(request, id):
    course = Course.objects.get(id=id)
    context = {
        'course': course
    }
    return render(request, 'delete_alert.html', context)

def delete_course(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('/')