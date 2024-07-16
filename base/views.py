from django.shortcuts import render

# Create your views here.

rooms = [
    {'id':1, 'name':'Find an organization'},
    {'id':2, 'name':'Get a referral'},
    {'id':3, 'name':'Find a job opening'},
    {'id':4, 'name':'Get your resume reviewed'}
]


def home(request):
    return render(request, 'home.html', {'rooms': rooms})
    # The templates folder is searched for home.html

def room(request):
    return render(request, 'rooms.html')
