
from django.urls import path
from catalog.views import  home, contact, ProductListView, ProductDetailView,  ProductCreateView, ProductUpdateView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='catalog'),
    path('contacts', home, name='home'),
    path('contact/', contact, name='contact'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
]
