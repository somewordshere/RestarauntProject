from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addItem/', views.addItem, name='addItem'),
    path('addItem/addItemSubmit/', views.addItemSubmit, name='addItemSubmit'),
    path('deleteItem/<int:id>', views.deleteItem, name='deleteItem'),
    path('updateItem/<int:id>', views.updateItem, name="updateItem"),
    path('updateItem/updateItemSubmit/<int:id>', views.updateItemSubmit, name="updateItemSubmit"),
]