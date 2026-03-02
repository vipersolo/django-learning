from django.shortcuts import render

# Create your views here.
def hello_view(request):
    context = {"name":"antony"}
    return render(request,"shop/welcome.html",context)

def home_view(request):
    return render(request,"shop/home.html")