from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('dashboard/',views.dashboard_redirect,name='dashboard_redirect'),
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/employee/', views.employee_dashboard, name='employee_dashboard'),
    path('dashboard/technician/', views.technician_dashboard, name='technician_dashboard'),
    path('dashboard/technician/', views.technician_dashboard, name='technician_dashboard'),
    path('ticket/<int:ticket_id>/update/<str:new_status>/', views.update_ticket_status, name='update_ticket_status'),
    path('assets/', views.asset_list, name='asset_list'),
    path('assets/add/', views.asset_create, name='asset_create'),
    path('assets/edit/<int:pk>/', views.asset_edit, name='asset_edit'),
    path('assignments/', views.assignment_list, name='assignment_list'),
    path('assignments/new/', views.assign_asset, name='assign_asset'),
    path('assignments/return/<int:pk>/', views.return_asset, name='return_asset'),
    path('inventory/', views.inventory_list, name='inventory_list'),
    path('inventory/update/<int:pk>/<str:action>/', views.update_stock, name='update_stock'),
    path('my-assets/', views.my_assets, name='my_assets'),
    path('asset/<int:asset_id>/report/', views.report_issue, name='report_issue'),
    path('admin/repairs/', views.manage_repairs, name='manage_repairs'),
    path('admin/repairs/assign/<int:ticket_id>/', views.assign_technician, name='assign_technician'),
]

