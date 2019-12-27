from django.shortcuts import render
from .models import Getdata

# Create your views here.

def get(request):
    return render(request, 'get.html')

def get_response(request):
    data = Getdata()
    data.name = request.GET['name']
    data.tel = request.GET['tel']
    data.save()

    alldata = Getdata.objects.all()
    context = {
        'alldata' : alldata,
    }
    return render(request, 'post.html' , context )


def post(request):
    return ''