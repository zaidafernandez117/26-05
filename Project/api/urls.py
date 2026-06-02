
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='inicio'),
    # path ('registro/',Registro,name='Registro'),
]
