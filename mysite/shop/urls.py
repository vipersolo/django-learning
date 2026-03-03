from django.urls import path
from . import views

# from .views import hello_view

urlpatterns = [
    path('',views.home_view,name="home"),
    path('welcome/',views.hello_view,name="hello"),
    path('base/',views.base_view,name='base'),
    path('inherited/',views.inherited_view,name='inherited'),
    path('contact/',views.contact_view,name='contact')
]
