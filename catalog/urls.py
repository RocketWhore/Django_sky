
from django.urls import path
from catalog.views import index, home, contact
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='catalog'),
    path('contacts', home, name='home'),
    path('contact/', contact, name='contact')
]
