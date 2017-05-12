from django.conf.urls import url
from django.views.generic.base import TemplateView

from FETraining.views import AuthorListCreateAPIView, \
    AuthorRetrieveUpdateDestroyAPIView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="book_index.html")),
    url(r'^author/', AuthorListCreateAPIView.as_view()),
    url(r'^author/(?P<id>[0-9]+)/',
        AuthorRetrieveUpdateDestroyAPIView.as_view()),
]
