from rest_framework import serializers

from FETraining.models import Author, Book, Publisher


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
