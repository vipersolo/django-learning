from django.urls import path
from . import views
from .views import Myview

urlpatterns= [
    path('register/',views.register_user),
    path('',views.home,name='home'),
    path('checkpost/',views.check_post,name='check_post'),
    path('delete/<int:item_id>/',views.delete_post,name='delete_post'),
    path('classbasedview/',Myview.as_view(),name='Myview')
]

