from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'd_index.html')
def ex1(request):
    return render(request, 'dom_ex1.html')    
def ex2(request):
    return render(request, 'dom_ex2.html')    