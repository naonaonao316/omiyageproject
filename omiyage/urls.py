from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('grid', views.grid, name='grid'),
    path('grid2', views.grid2, name='grid2'),
]
