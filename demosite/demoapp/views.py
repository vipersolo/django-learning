from django.http import HttpResponse
import threading
import time
from django.views.decorators.csrf import csrf_exempt
def send_email(user,email):
    time.sleep(5)
    print("email send.")

def register_user(request):
    name = 'antony'
    email = 'antony@example.com'

    t=threading.Thread(target=send_email,args=(name,email))
    t.start()
    return HttpResponse("email sending in background ...")

def home(request):
    return HttpResponse("welcome to Home")

@csrf_exempt #used to disable csrf to check fucntion with post(use from django.views.decorators.csrf import csrf_exempt).
def check_post(request):
    if request.method == 'POST':
        data = request.POST
        return HttpResponse(f"the Data are:{data}")
    
    return HttpResponse("This is GET request") #always return in invalid case also with reason or django throws error.