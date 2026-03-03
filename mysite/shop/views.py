from django.shortcuts import render

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