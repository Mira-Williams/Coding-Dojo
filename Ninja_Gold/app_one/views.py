from django.shortcuts import render, redirect
import random
import time
from datetime import datetime

def index(request):
    if 'high_score' not in request.session:
        request.session['high_score'] = 0
    if request.session['gold'] > request.session['high_score']:
        request.session['high_score'] = request.session['gold']
    return render(request, 'app_one/index.html')

def cave(request):
    time.sleep(1)
    if request.session['cave_count'] <= 2:
        loot = random.randint(1,50)
        request.session['loot'] = loot
        request.session['gold'] += loot
        log = 'You found ' + str(loot) + ' gold in the cave! - (' + str(datetime.now().strftime("%b %d, %Y, %-I:%M%p")) + ' )'
        request.session['log'].append(log)
        request.session['cave_count'] += 1
    else:
        temp_list = request.session['log']
        log = 'There is no more gold in the cave.'
        temp_list.append(log)
        request.session['log'] = temp_list
    return redirect('/')

def castle(request):
    time.sleep(1)
    if request.session['castle_count'] <= 2:
        loot = random.randint(1,50)
        request.session['loot'] = loot
        request.session['gold'] += loot
        log = 'You found ' + str(loot) + ' gold in the castle!'
        request.session['log'].append(log)
        request.session['castle_count'] += 1
    else:
        temp_list = request.session['log']
        log = 'There is no more gold in the castle.'
        temp_list.append(log)
        request.session['log'] = temp_list
    return redirect('/')
    
def ship(request):
    time.sleep(1)
    if request.session['ship_count'] <= 2:
        loot = random.randint(1,50)
        request.session['loot'] = loot
        request.session['gold'] += loot
        log = 'You found ' + str(loot) + ' gold in the shipwreck!'
        request.session['log'].append(log)
        request.session['ship_count'] += 1
    else:
        temp_list = request.session['log']
        log = 'There is no more gold in the shipwreck.'
        temp_list.append(log)
        request.session['log'] = temp_list
    return redirect('/')

def casino(request):
    time.sleep(1)
    win_or_loss = random.randint(0,1)
    # win_or_loss = 1
    if win_or_loss == 1:
        win_percent = random.choice([0.5, 1])
        winnings = round(request.session['gold'] * win_percent)
        request.session['gold'] += round(request.session['gold'] * win_percent)
        log = 'You won ' + str(winnings) + ' gold in the casino!'
        request.session['log'].append(log)
    else:
        loss_percent = random.choice([0.5, 1])
        loss = round(request.session['gold'] * loss_percent)
        request.session['gold'] -= round(request.session['gold'] * loss_percent)
        log = 'You lost ' + str(loss) + ' gold in the casino :('
        request.session['log'].append(log)
    return redirect('/')

def reset(request):
    # request.session.flush()
    request.session['log'] = []
    request.session['gold'] = 0
    request.session['cave_count'] = 0
    request.session['castle_count'] = 0
    request.session['ship_count'] = 0
    return redirect('/')

# def cave(request):
#     chance_find_gold = random.randint(1,6)
#     if chance_find_gold == 1:
#         loot = random.randint(0,50)
#         request.session['loot'] = loot
#         if 'gold' not in request.session:
#             request.session['gold'] = 0
#             request.session['gold'] += loot
#         else:
#             request.session['gold'] += loot
#         log = 'You found ' + str(loot) + ' gold in the cave!'
#         if 'log' not in request.session:
#             # request.session['log'] = []
#             request.session['log'].append(log)
#         else:
#             request.session['log'].append(log)
#     else:
#         log = "You found no gold in the cave."
#         if 'log' not in request.session:
#             # request.session['log'] = []
#             request.session['log'].append(log)
#         else:
#             request.session['log'].append('poop')
#     return render(request, 'app_one/index.html')

# def castle(request):
#     loot = random.randint(0,50)
#     request.session['loot'] = loot
#     if 'gold' not in request.session:
#         request.session['gold'] = 0
#         request.session['gold'] += loot
#     else:
#         request.session['gold'] += loot
#     log = 'You found ' + str(loot) + ' gold in the castle!'
#     if 'log' not in request.session:
#         request.session['log'] = []
#         request.session['log'].append(log)
#     else:
#         request.session['log'].append(log)
#     return render(request, 'app_one/index.html')

# def cave(request):
#     time.sleep(1)
    # if request.session['next_winner'] == 'cave':
        # loot = random.randint(1,50)
        # request.session['loot'] = loot
        # request.session['gold'] += loot
        # log = 'You found ' + str(loot) + ' gold in the cave!'
        # request.session['log'].append(log)
        # cave_count
    # else:
    #     log = 'You found no gold in the cave.'
    #     temp_list = request.session['log']
    #     temp_list.append(log)
    #     request.session['log'] = temp_list
    # return render(request, 'app_one/index.html')

    # winner_list = ['cave', 'castle', 'ship']
    # next_winner = random.choice(winner_list)
    # request.session['next_winner'] = next_winner