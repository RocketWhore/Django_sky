
from django.urls import path
from catalog.views import  home, contact, ProductListView, ProductDetailView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='catalog'),
    path('contacts', home, name='home'),
    path('contact/', contact, name='contact'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
]
