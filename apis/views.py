# Django imports
from django.shortcuts import render
from django.db import connection

# Rest Framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Book
from .serializers import BookSerializer

class BookView(APIView):  # Cambié el nombre de la clase a BookView

    def post(self, request, format=None):
        
        serializer = BookSerializer(data=request.data)
        
        if serializer.is_valid():  
            
            serializer.save()  

            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

    def get(self, request, pk):

        book = get_object_or_404(Book, pk=pk)

        serializer = BookSerializer(book)

        return Response(serializer.data)
    
    def put(self, request, pk):
        
        book = get_object_or_404(Book, pk=pk) 

        serializer = BookSerializer(book, data=request.data)  

        if serializer.is_valid():  
            
            serializer.save()  

            return Response(serializer.data) 

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
    def delete(self, request, pk):
        
        book = get_object_or_404(Book, pk=pk)  
        
        book.delete()  
        
        return Response(status=status.HTTP_204_NO_CONTENT)  
