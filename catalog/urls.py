
from django.urls import path
from catalog.views import index, home

urlpatterns = [
    path('contacts', index, name='catalog'),
    path('', home, name='home'),
]
