from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import random

def main(request):  

    filter_count = 0
    chapter_final = []
    verse_choice = []

    if request.method == 'POST':
        if 'Old_Test' in request.POST:
            filter_books = Book.objects.filter(Old_Test=True)
            filter_count += 1
        if 'New_Test' in request.POST:
            filter_books = Book.objects.filter(New_Test=True)
            filter_count += 1
        if 'Gospels' in request.POST:
            filter_books = Book.objects.filter(Gosp=True)
            filter_count += 1
        if 'Pentateuch' in request.POST:
            filter_books = Book.objects.filter(Pent=True)
            filter_count += 1
        if 'book_ot' in request.POST:
            if request.POST['book_ot'] != '':
                book_ot = request.POST['book_ot']
                filter_books = Book.objects.filter(Name=book_ot)
                filter_count += 1
        if 'book_nt' in request.POST:
            if request.POST['book_nt'] != '':
                book_nt = request.POST['book_nt']
                filter_books = Book.objects.filter(Name=book_nt)
                filter_count += 1
        
    if filter_count > 1:
        messages.error(request, 'Please choose only 1 option.')
        return redirect('/no_choice')
    

    if Book.objects.all():
        if filter_count == 0:
            filter_books = Book.objects.all()
        weight_list = []
        for current_book in filter_books:
            weight_list.append(current_book.num_verses)
        book_choice = random.choices(filter_books, weights=weight_list, k=1)
        book_name = book_choice[0].Name

        filter_chapters = Chapter.objects.filter(Book=book_name)

        chapter_weights = []
        for current_chapter in filter_chapters:
            chapter_weights.append(current_chapter.num_verses)
        chapter_choice = random.choices(filter_chapters, weights=chapter_weights, k=1)

        chapter_final = chapter_choice[0]
        

        verse_choice = random.randint(1, chapter_final.num_verses)

        context={
            'chapter': chapter_final,
            'verse': verse_choice,
        }


        return render(request, 'main.html', context)
    
    else:
        messages.error(request, 'Please initialize Bible database.')
        return render(request, 'main.html')



def delete_all(request):
    Book.objects.all().delete()
    return redirect('/')

def no_choice(request):
    return render(request, 'main.html')