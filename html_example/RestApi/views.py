from django.shortcuts import render

# Create your views here.

def get(request):
    return render(request, 'get.html')

def get_response(request):
    return render(request, 'post.html')

def post(request):
    return ''