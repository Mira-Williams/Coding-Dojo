from django.shortcuts import render, HttpResponse
import pytz
import datetime

def currentDateTime(request):
    tzPac = pytz.timezone('US/Pacific')
    tzMtn = pytz.timezone('US/Mountain')
    tzCen = pytz.timezone('US/Central')
    tzEst = pytz.timezone('US/Eastern')

    currDTP = datetime.datetime.now(tz=tzPac)
    currDTM = datetime.datetime.now(tz=tzMtn)
    currDTC = datetime.datetime.now(tz=tzCen)
    currDTE = datetime.datetime.now(tz=tzEst)

    currDate = currDTP.strftime('%B %d, %Y')
    currTimeP = currDTP.strftime('%-I:%M %p')
    currTimeM = currDTM.strftime('%-I:%M %p')
    currTimeC = currDTC.strftime('%-I:%M %p')
    currTimeE = currDTE.strftime('%-I:%M %p')

    context = {
        'currDate': currDate,
        'currTimeP': currTimeP,
        'currTimeM': currTimeM,
        'currTimeC': currTimeC,
        'currTimeE': currTimeE
    }
    return render(request, 'index.html', context)





    
