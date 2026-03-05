from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group
from django.contrib.auth.decorators import user_passes_test
# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'employee/register.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request,'employee/login.html',{'form':form})


@login_required
def home_view(request):
    return render(request,'employee/home.html')

def logout_view(request):
    logout(request)
    return redirect('login')

user = User.objects.get(username="john")
group = Group.objects.get(name="Manager")
user.groups.add(group)

user = User.objects.get(username="employee1")
group = Group.objects.get(name="Employee")
user.groups.add(group)

user = User.objects.get(username="root")
group = Group.objects.get(name="Admin")
user.groups.add(group)

def is_admin(user):
    return user.groups.filter(name="Admin").exists()
def is_manager(user):
    return user.groups.filter(name="Manager").exists()
def is_employee(user):
    return user.groups.filter(name="Employee").exists()

@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request,"employee/admin_dashboard.html")

@user_passes_test(is_manager)
def manager_dashboard(request):
    return render(request,"employee/manager_dashboard.html")

@user_passes_test(is_employee)
def employee_dashboard(request):
    return render(request,"employee/employee_dashboard.html")
