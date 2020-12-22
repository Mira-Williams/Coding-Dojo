from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt


def login_page(request):
    return render(request, 'login_page.html')

def register(request):
    user = User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    )
     
    messages.success(request, 'New user created')

    return redirect('/')

def login_user(request):
    user_match = User.objects.filter(email=request.POST['email'])

    if len(user_match) > 0:
        if bcrypt.checkpw(request.POST['password'].encode(), user_match[0].password.encode()):
            request.session['login_id'] = user_match[0].id
            request.session['login_first_name'] = user_match[0].first_name
            return redirect('/main')
        else:
            messages.error(request, 'Incorrect password')
            return redirect('/')
    else:
        messages.error(request, 'Email not registered')
        return redirect('/')

def main(request):
    if 'login_id' in request.session:
        context={
            'books': Book.objects.all(),
            'user': User.objects.get(id=request.session['login_id'])
        }
        return render(request, 'main.html', context)
    else:
        messages.error(request, 'Must login first')
        return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

def create_book(request):
    user = User.objects.get(id = request.session['login_id'])

    book = Book.objects.create(
        title = request.POST['title'],
        description = request.POST['description'],
        added_by = user
    )

    user.favorite_books.add(book)

    return redirect('/main')

def book_page(request, book_id):
    user = User.objects.get(id=request.session['login_id'])
    context = {
        'book': Book.objects.get(id=book_id),
        'user': user
    }
    return render(request, 'book_page.html', context)

def add_to_favs(request, book_id):
    user = User.objects.get(id = request.session['login_id'])
    book = Book.objects.get(id=book_id)
    user.favorite_books.add(book)

    context={
        'books': Book.objects.all(),
        'user': user
    }

    return render(request, 'main.html', context)

def del_from_favs(request, book_id):
    user = User.objects.get(id = request.session['login_id'])
    book = Book.objects.get(id=book_id)
    user.favorite_books.remove(book)

    context={
        'books': Book.objects.all(),
        'user': user
    }

    return render(request, 'main.html', context)

def only_favs(request):
    user = User.objects.get(id=request.session['login_id'])
    fav_books = user.favorite_books.all()

    context={
        'fav_books': fav_books,
        'user': user
    }

    return render(request, 'only_favs.html', context)

def edit_page(request, book_id):
    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=request.session['login_id'])
    context={
        'book': book,
        'user': user
    }

    return render(request, 'edit_page.html', context)

def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.description = request.POST['description']
    book.save()

    return redirect(f'/book_page/{book.id}')