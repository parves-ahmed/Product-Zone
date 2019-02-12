from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.create_item, name='create'),
    path('details/', views.details_item, name='details'),
    path('update/<int:id>/', views.update_item, name='update'),
    path('delete/<int:id>/', views.delete_item, name='delete'),
]