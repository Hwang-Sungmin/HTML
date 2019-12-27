from django.urls import path
from . import views as restapi_views

app_name = 'restapi'

urlpatterns = [
    path('get/', restapi_views.get, name="get"),
    path('response/', restapi_views.get_response, name="getR"),
    path('post/', restapi_views.post, name="post"),
]
