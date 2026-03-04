from django.shortcuts import render,redirect
from .forms import ContactForm,EmployeeForms
from .models import Employee

# Create your views here.
def hello_view(request):
    context = {"name":"antony","age":20}
    return render(request,"shop/welcome.html",context)

def home_view(request):
    context = {"value":5000,"age":25}
    return render(request,"shop/home.html",context)

def base_view(request):
    return render(request,'base.html')

def inherited_view(request):
    return render(request,'shop/inherited.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            print(f"{name},{email},{message}")

            return render(request,'shop/thankyou.html',{'name':name,'email':email,'message':message})
        
    else:
        form = ContactForm()
        return render(request,'shop/contact.html',{'form':form})
    

def employee_register(request):
    if request.method == "POST":
        form = EmployeeForms(request.POST)
        if form.is_valid():
            employeeobj = Employee.objects.create(
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                email = form.cleaned_data['email'],
                department = form.cleaned_data['department'],
            )
            return redirect('success',pk=employeeobj.pk)
    else:
        form = EmployeeForms()
    return render(request,'shop/register.html',{'form':form}) # if validation fails, 'form' is from POST,not else (in order to show errors), refresh just does the last request , ie post, errors should'nt go away.

    
def success(request,pk):
    current_user_details = Employee.objects.get(pk=pk)
    return render(request,'shop/success.html',{'current_user_details':current_user_details})