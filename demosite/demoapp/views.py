from django.http import HttpResponse, HttpResponseNotAllowed
import threading
import time
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator
import json
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
    
    return HttpResponse("This is GET request") #always return invalid case also with reason or django throws error eg(if post not found return also for get.).

@csrf_exempt #also need to disable cross site request forge protection
def delete_post(request,item_id):
    if request.method == "DELETE":
        # item_id = request.GET.get("id") #query parameter style , use rest style-> industry standard.
        return HttpResponse(f"Deleted item :{item_id}")
    return HttpResponseNotAllowed(['DELETE'])

@method_decorator(csrf_exempt,name='dispatch')
class Myview(View):
    def get(self,request):
        return HttpResponse("this is a get request managed by django automatically.")
    
    def post(self,request):
        return HttpResponse("this is a post request managed by django automatically.")
    
    def put(self,request):
        body = request.body
        data= json.loads(body)
        return HttpResponse(f"data : {data}")
    
    def delete(self,request):
        return HttpResponse(f"delete request recived.")
    
