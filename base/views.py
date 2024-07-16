from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
    # The templates folder is searched for home.html

def jobs(request):
    return render(request, 'jobs.html')
