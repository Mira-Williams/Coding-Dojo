from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages


def index(request):
    return redirect('/home')

def home(request):
    shows = Show.objects.all()
    context = {
        'shows': shows
    }
    return render(request, 'index.html', context)

def add_form(request):
    return render(request, 'add_form.html')

def add_show(request):
    if request.method == 'POST':
        errors = Show.objects.validate(request.POST)
        context = {
            'title': request.POST['title'],
            'network': request.POST['network'],
            'release_date': request.POST['release_date'],
            'description': request.POST['description']
        }
        if errors:
            for error in errors:
                messages.error(request, error)
            # return redirect('/add_form')
            return render(request, 'add_form.html', context)
        show = Show.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            release_date = request.POST['release_date'],
            description = request.POST['description'],
        )
    return redirect('/home')
    

def single_show_page(request, id):
    show = Show.objects.get(id=id)
    context = {
        'show': show
    }
    return render(request, 'single_show.html', context)

def edit_show_form(request, id):
    show = Show.objects.get(id=id)
    context = {
        'show': show
    }
    return render(request, 'edit_form.html', context)

def update_show(request, id):
    if request.method == 'POST':
        errors = Show.objects.validate_update(request.POST, id)
        if errors:
            for error in errors:
                messages.error(request, error)
                return redirect(f'/edit_show_form/{id}')
        else:
            show = Show.objects.get(id=id)
            show.title = request.POST['title']
            show.network = request.POST['network']
            show.release_date = request.POST['release_date']
            show.description = request.POST['description']
            show.save()
            return redirect(f'/single_show/{id}')

def delete_alert(request, id):
    show = Show.objects.get(id=id)
    context = {
        'show': show
    }
    return render(request, 'delete_alert.html', context)

def delete_show(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect('/home')