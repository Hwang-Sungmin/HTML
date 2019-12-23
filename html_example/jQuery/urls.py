from django.urls import path
from . import views as jq_views

urlpatterns = [
    path('', jq_views.index, name='index'),
    path('event', jq_views.event, name='event'),
    path('ajax', jq_views.ajax_ex, name='ajax_ex'),
    path('json', jq_views.json, name='json'),
    
]
