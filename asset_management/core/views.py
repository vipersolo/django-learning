from django.http import HttpResponse

def home(request):
    return HttpResponse("Asset Management System Running ✅")