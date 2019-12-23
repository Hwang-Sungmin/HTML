from django.shortcuts import render

# Create your views here.

def index(reqeust):
    return render(reqeust, 'index.html')

def event(reqeust):
    return render(reqeust, 'event.html')

def ajax_ex(reqeust):
    return render(reqeust, 'ajax_ex.html')

def json(reqeust):
    return render(reqeust, 'json.html')