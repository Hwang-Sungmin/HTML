from django.urls import path
from . import views as views_onclick

app_name = 'onclick'

urlpatterns = [
    path('', views_onclick.index, name="index"),
    
   
]
