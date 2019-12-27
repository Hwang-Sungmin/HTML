#### GET과 POST 방식 주고받기

 -  appname을 적어줘야지 html에서 url  위치를 찾을 수 있다.

     - html : get으로 보내기 연습

    ~~~~html
    <body>
        <form method="get" action="{% url 'restapi:getR' %}"> 
            <input type="text" name="name" placeholder="Enter id here">
            <input type="text" name="tel" placeholder="Enter telephone# here">
            <input type="submit" value="Submit">

        </form>
    </body>
    ~~~~

    - **urls.py 부분**

    ~~~~python
    from django.urls import path
    from . import views as restapi_views

    app_name = 'restapi'

    urlpatterns = [
        path('get/', restapi_views.get, name="get"),
        path('response/', restapi_views.get_response, name="getR"),
        path('post/', restapi_views.post, name="post"),
    ]
    ~~~~



####  Modeld을 만들어 값을 저장 그리고 다른 html에 페이지에 보내기

