from django.urls import path
from . import views

# from .views import hello_view

urlpatterns = [
    path('',views.home_view,name="home"),
    path('welcome/',views.hello_view,name="hello")
]
