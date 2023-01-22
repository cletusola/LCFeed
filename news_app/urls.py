from django.urls import path 
from .views import HomeView,getData

urlpatterns = [
    path('', HomeView, name='Home'),
    path('get_data/',getData, name='get_data')
    # path('abc/',funcView, name='func'),
]
