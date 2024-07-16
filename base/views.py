from django.shortcuts import render
from .models import Room
# Create your views here.

rooms = [
    {'id':1, 'name':'Find an organization'},
    {'id':2, 'name':'Get a referral'},
    {'id':3, 'name':'Find a job opening'},
    {'id':4, 'name':'Get your resume reviewed'}
]


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)
    # The templates folder is searched for home.html

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    
    return render(request, 'base/rooms.html', context)
