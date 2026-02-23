from django.urls import path
from . import views

urlpatterns= [
    path('register/',views.register_user),
    path('',views.home,name='home'),
    path('checkpost/',views.check_post,name='check_post')
]

