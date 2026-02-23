from django.http import HttpResponse
import threading
import time

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