from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('getAll', views.getAll, name='getAll'),
    path('insert', views.insert, name='insert'),
    path('get/<int:id>', views.get, name='get'),
    path('search', views.search, name='search'),
    path('drop/<int:id>', views.drop, name='drop'),
]

