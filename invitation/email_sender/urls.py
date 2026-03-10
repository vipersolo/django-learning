from django.urls import path
from . import views

urlpatterns = [
    path("",views.home_page,name="home_page"),
    path("send/",views.send_test_mail,name="send_test_mail"),
    path("test/",views.test,name="test"),
    
    
]