from django.http import HttpResponse
from django.shortcuts import render
from random import randint
from password.password_gen import passwordgen

def home(request):
    data = {'password': passwordgen()}
    return render(request, 'home.html', data)
