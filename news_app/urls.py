from django.urls import path 
from .views import HomeView
# ,getData

urlpatterns = [
    path('', HomeView, name='Home'),
]
