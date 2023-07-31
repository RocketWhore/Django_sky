from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import *


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
# def index(request):
#     product_list = Product.objects.all()
#     content = {
#         'object_list': product_list,
#         'category_list': Category.objects.all()
#     }
#     return render(request, 'catalog/home.html', content)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name}\n{email}\n{message}')
    return render(request, 'catalog/contact.html')

def home(request):
    if request.method == 'GET':
        # name = request.POST.get('name')
        # email = request.POST.get('email')
        # message = request.POST.get('message')
        # print(f'{name}\n{email}\n{message}')
        return render(request, 'catalog/index.html')

# def product(request, pk):
#     item = Product.objects.get(pk=pk)
#
#     context = {
#         'object': item,
#
#     }
#     return render(request, 'catalog/product.html', context=context)