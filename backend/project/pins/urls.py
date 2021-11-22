from django.urls import path
from .views import home, create_pin, save_pin

urlpatterns = [

    path('home/', home, name='home'),
    path('create/', create_pin, name='create'),
    path('save/', save_pin, name='save'),
]