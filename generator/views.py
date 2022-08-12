import re
from django.shortcuts import render
from django.http import HttpResponse
import random
from string import ascii_lowercase, ascii_uppercase

# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password': 'sndjfone0823h89hbgue'})

def password(request):  
    characters = list(ascii_lowercase)
    
    if request.GET.get('uppercase'):
        characters.extend(list(ascii_uppercase))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend('1234567890')
    
    length = int(request.GET.get('length', 12))
    
    the_password = ''
    for _ in range(length):
        the_password += random.choice(characters)
    
    return render(request, 'generator/password.html', {'password': the_password})

def about(request):
    return render(request, 'generator/about.html')

def username(request):
    first_name = request.GET.get('first_name').title()
    last_name = request.GET.get('last_name').lower()
    
    username = first_name[0] + last_name
    
    return render(request, 'generator/username.html', {'username': username})