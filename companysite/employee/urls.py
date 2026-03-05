from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('home/',views.home_view,name='home'),
    path('logout/',views.logout_view,name='logout'),
    path('admin-dashboard/',views.admin_dashboard,name="admin_dashboard"),
    path('manager_dashboard/',views.manager_dashboard,name="manager_dashboard"),
    path('employee_dashboard/',views.employee_dashboard,name="employee_dashboard"),
]