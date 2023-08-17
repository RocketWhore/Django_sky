from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from catalog.forms import ProductForm, VersionForm
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


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog')

    def get_object(self, queryset=None):
        return self.request.user


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        version_formset = inlineformset_factory(self.model, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = version_formset(self.request.POST, instance=self.object)
        else:
            formset = version_formset(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        with transaction.atomic():
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()
        return super().form_valid(form)
# class ProductUpdateView(UpdateView):
#     model = Product
#     form_class = ProductForm
#     success_url = reverse_lazy('catalog:catalog')
#
#     def get_context_data(self, **kwargs):
#         context_data = super().get_context_data(**kwargs)
#         VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
#         if self.request.method == 'POST':
#             context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
#         else:
#             context_data['formset'] = VersionFormset(instance=self.object)
#         return context_data
#
#     def form_valid(self, form):
#         formset = self.get_context_data()['formset']
#         self.object = form.save
#         if formset.is_valid():
#             formset.instance = self.object
#             form.save()
#
#         return super().form_valid(form)

# def product(request, pk):
#     item = Product.objects.get(pk=pk)
#
#     context = {
#         'object': item,
#
#     }
#     return render(request, 'catalog/product.html', context=context)
