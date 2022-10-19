from django.shortcuts import render
from .models import product
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.


@login_required
def profile(request):
    return render(request, 'users/profile.html')



def index(request):
    products = product.objects.order_by('id')[:3]
    content = {
        "products":products
    }
    return render(request, 'index.html', content)


def product_details(request, pk):  
    products = product.objects.get(id=pk)
    context = {
        "product":products
    }
    return render(request, 'product_details.html', context)


def product_list(request):
    products = product.objects.all()
    content = {
        "products":products
    }
    return render(request, "product_list.html", content)


   