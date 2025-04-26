from django.shortcuts import render
from .models import Boat
# Create your views here.

def home(request):
    return render(request, 'home.html')

def boats(request):
    boats_list = Boat.objects.all()
    return render(request, 'boats.html', {'boats': boats_list})