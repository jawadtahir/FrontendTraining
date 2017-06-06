from django.conf.urls import url
from django.views.generic.base import TemplateView

from FETraining.views import *

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="book_index.html")),
    url(r'^api/author/', AuthorListCreateAPIView.as_view()),
    url(r'^api/author/(?P<id>[0-9]+)/',
        AuthorRetrieveUpdateDestroyAPIView.as_view()),
    url(r'^api/name/', NameListCreateAPIView.as_view()),
    url(r'^api/name/(?P<id>[0-9]+)/',
        AuthorRetrieveUpdateDestroyAPIView.as_view()),
    url(r'^api/contact/', ContactListCreateAPIView.as_view()),
    url(r'^api/contact/(?P<id>[0-9]+)/',
        ContactRetrieveUpdateDestroyAPIView.as_view()),
    url(r'^api/publisher/', PublisherListCreateAPIView.as_view()),
    url(r'^api/author/(?P<id>[0-9]+)/',
        PublisherRetrieveUpdateDestroyAPIView.as_view()),
    url(r'^api/book/', BookListCreateAPIView.as_view()),
    url(r'^api/book/(?P<id>[0-9]+)/',
        BookRetrieveUpdateDestroyAPIView.as_view()),
]
