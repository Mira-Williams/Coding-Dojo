from django.shortcuts import render

def form_survey(request):
    return render(request, 'form.html')

def results(request):
    context = {
        'name': request.POST['name'],
        'language': request.POST['language'],
        'location': request.POST['location'],
        'hobbies': request.POST['hobbies']
    }
    return render(request, 'results.html', context)