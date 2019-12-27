from django.shortcuts import render
from .models import Getdata

# Create your views here.

def get(request):
    return render(request, 'get.html')


# get방식과 post 방식을 경량 db에 저장
def get_response(request):
    if request.method == "GET":
        data = Getdata()
        data.name = request.GET['name']
        data.tel = request.GET['tel']
        data.save()

        alldata = Getdata.objects.all()
        context = {
            'alldata' : alldata,
        }
        return render(request, 'get_response.html' , context )

    else:
        data = Getdata()
        data.name = request.POST['name']
        data.tel = request.POST['tel']
        data.save()

        alldata = Getdata.objects.all()
        context = {
            'alldata' : alldata,
        }
        return render(request, 'post_response.html', context )

def post(request):
    return render(request, 'post.html')