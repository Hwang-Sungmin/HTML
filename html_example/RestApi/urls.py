from django.urls import path
from . import views as restapi_views

app_name = 'restapi'

urlpatterns = [
    path('get/', restapi_views.get, name="get"),
    #여기서 get과 post 방식 한 번에 처리하기 
    path('response/', restapi_views.get_response, name="getR"),
    path('post/', restapi_views.post, name="post"),
]
