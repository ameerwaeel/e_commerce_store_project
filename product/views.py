from django.shortcuts import render ,get_object_or_404
from .models import *
from django.core.paginator import Paginator

# Create your views here.
def product_list(request):
    product_list=Product.objects.all()

    paginator = Paginator(product_list, 6)  # Show 10 objects per page
    page_number = request.GET.get('page')
    product_list = paginator.get_page(page_number)  # Returns the page object
    
    context={'product_list':product_list,
            #  'page_obj':page_obj
             }
    return render(request,'product_list.html',context)



def product_detail(request,slug):
    product_detail=get_object_or_404(Product, PRDSlug=slug)

    



    context={'product_detail':product_detail}
    return render(request,'product_detail.html',context)    