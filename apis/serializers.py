from rest_framework import serializers

from .models import Book

class BookSerializer(serializers.ModelSerializer):

    class Meta:

        model = Book  # Indica qué modelo vas a serializar

        fields = '__all__'  # Puedes especificar los campos que quieres serializar o usar '__all__' para todos
