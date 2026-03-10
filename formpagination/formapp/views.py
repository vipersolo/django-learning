from django.shortcuts import render
from.models import Product
from django.core.paginator import Paginator
# Create your views here.

def product_list(request):
    products = Product.objects.all()
    query = request.GET.get("q","")
    if query:
        products = Product.objects.filter(name__icontains=query)

    paginator = Paginator(products,5)
    page_numer = request.GET.get("page")
    page_obj = paginator.get_page(page_numer)

    return render(request,'formapp/product_list.html',{'page_obj':page_obj,"query":query})

    
