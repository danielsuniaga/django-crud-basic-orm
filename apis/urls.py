# apis/urls.py
from django.urls import path
from .views import BookView  # Asegúrate de importar la vista correctamente

urlpatterns = [

    path('create/', BookView.as_view()),  

    path('get/<int:pk>/', BookView.as_view()), 

    path('update/<int:pk>/', BookView.as_view()),  

    path('delete/<int:pk>/', BookView.as_view()), 

]
