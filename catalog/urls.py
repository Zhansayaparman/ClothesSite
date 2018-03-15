from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clothes/', views.ClothesListView.as_view(), name='clothes'),
    path('clothes/<int:pk>', views.ClothesDetailView.as_view(), name='clothes-detail'),
    path('firmas/', views.FirmaListView.as_view(), name='firmas'),
    path('firma/<int:pk>', views.FirmaDetailView.as_view(), name='firma-detail'),
]