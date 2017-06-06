from django.forms.models import BaseModelFormSet

from FETraining.models import Author, Name, Contact, Publisher, Book


class AuthorForm(BaseModelFormSet):
    class Meta:
        model = Author


class NameForm(BaseModelFormSet):
    class Meta:
        model = Name


class ContactForm(BaseModelFormSet):
    class Meta:
        model = Contact


class PublisherForm(BaseModelFormSet):
    class Meta:
        model = Publisher


class BookForm(BaseModelFormSet):
    class Meta:
        model = Book
