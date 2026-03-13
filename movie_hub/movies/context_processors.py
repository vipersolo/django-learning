from .models import Catergory

def categories_processor(request):
    return {
        "categories":Catergory.objects.all()
    }