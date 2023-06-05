from django.urls import path
from .views import home,create_view,edit_view,delete_view,read_view

urlpatterns = [
    path('', home, name='Home'),
    path('create/',create_view, name="Create"),
    path('edit/<str:pk>/',edit_view, name="Edit"),
    path('delete/<str:pk>/',delete_view, name="Delete"),
    path('note/<str:pk>/',read_view, name="Note")
]
