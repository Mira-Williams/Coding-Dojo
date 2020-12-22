from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string
from random_word import RandomWords
r = RandomWords()

def main(request):
    if 'attempt_num' not in request.session:
        request.session['attempt_num'] = 0
    request.session['attempt_num'] += 1
    # request.session['word'] = get_random_string(length=14)
    request.session['word'] = r.get_random_word(minLength=14, maxLength=14)
    return render(request, 'index.html')

def reset(request):
    request.session.flush()
    return redirect("/")