from django.shortcuts import render,redirect
from django.http.response import HttpResponse
import json

# Create your views here.

def index(request):
    return render(request, 'Onclick/main.html')

def find(request):
    if request.method == 'POST':
        input = request.POST['input']
        print(input)
        return HttpResponse('', status=204)