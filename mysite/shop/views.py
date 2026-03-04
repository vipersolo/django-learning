from django.shortcuts import render,redirect
from .forms import ContactForm,EmployeeForms

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
            form.save()
            return redirect('success')
    else:
        form = EmployeeForms()
    return render(request,'shop/register.html',{'form':form})
    
def success(request):
    return render(request,'shop/success.html')