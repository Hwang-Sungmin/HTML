from django.urls import path
from . import views as dom_views

urlpatterns = [
    path('', dom_views.index, name='d_index'),
    path('ex1/', dom_views.ex1, name='ex1'),
    path('ex2/', dom_views.ex2, name='ex2'),
    
]
