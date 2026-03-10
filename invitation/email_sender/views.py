from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# Create your views here.




def home_page(request):
    return render(request,"email_sender/home_page.html")


def send_test_mail(request):
    if request.method == "POST":
        email = request.POST.get("email")
        send_mail(
            "Invitation to join New Project",
            "Welcome to Newproject, let's go...",
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        return HttpResponse("email sent successfully")
    else:
        return render(request,"email_sender/home_page.html")
    

@csrf_exempt
def test(request):
    return HttpResponse("CSRF disabled")