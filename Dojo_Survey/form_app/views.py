from django.shortcuts import render, redirect, HttpResponse

def form_survey(request):
    return render(request, 'form.html')

def results(request):
    request.session['name'] = request.POST['name']
    request.session['language'] = request.POST['language']
    request.session['location'] = request.POST['location']
    request.session['hobbies'] = request.POST['hobbies']
    return redirect('/redir_funct')

def redir_funct(request):
    return render(request, 'results.html')
