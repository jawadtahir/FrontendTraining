from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from FETraining.models import Author, Book, Publisher, Name, Contact


class NameSerializer(ModelSerializer):
    class Meta:
        model = Name


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author


class PublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
