from django.contrib.auth.decorators import login_required
# Create your views here.
# Create your views here.
from django.utils.decorators import method_decorator
from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView

from FETraining.models import Author, Book, Name, Publisher, Contact
from FETraining.serializer import AuthorSerializer, BookSerializer, \
    PublisherSerializer, NameSerializer, ContactSerializer


@method_decorator(login_required(login_url="/"), 'get')
@method_decorator(login_required(login_url="/"), 'post')
class NameListCreateAPIView(ListCreateAPIView):
    queryset = Name.objects.all()
    serializer_class = NameSerializer


@method_decorator(login_required(login_url="/"), 'get')
@method_decorator(login_required(login_url="/"), 'patch')
@method_decorator(login_required(login_url="/"), 'put')
@method_decorator(login_required(login_url="/"), 'delete')
class NameRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Name.objects.all()
    serializer_class = NameSerializer


@method_decorator(login_required(login_url="/"), 'get')
@method_decorator(login_required(login_url="/"), 'post')
class ContactListCreateAPIView(ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


@method_decorator(login_required(login_url="/"), 'get')
@method_decorator(login_required(login_url="/"), 'patch')
@method_decorator(login_required(login_url="/"), 'put')
@method_decorator(login_required(login_url="/"), 'delete')
class ContactRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


@method_decorator(login_required(login_url="/"), 'get')
@method_decorator(login_required(login_url="/"), 'post')
class AuthorListCreateAPIView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get_renderer_context(self):
        rendered_context = super(AuthorListCreateAPIView, self).get_renderer_context()
        salutation_list = Name.get_salutations()
        rendered_context.update({'salutation_list': salutation_list})
        return rendered_context


@method_decorator(login_required(login_url="/"), 'get')
@method_decorator(login_required(login_url="/"), 'patch')
@method_decorator(login_required(login_url="/"), 'put')
@method_decorator(login_required(login_url="/"), 'delete')
class AuthorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


@method_decorator(login_required(login_url="/"), 'get')
@method_decorator(login_required(login_url="/"), 'post')
class PublisherListCreateAPIView(ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


@method_decorator(login_required(login_url="/"), 'get')
@method_decorator(login_required(login_url="/"), 'patch')
@method_decorator(login_required(login_url="/"), 'put')
@method_decorator(login_required(login_url="/"), 'delete')
class PublisherRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


@method_decorator(login_required(login_url="/"), 'get')
@method_decorator(login_required(login_url="/"), 'post')
class BookListCreateAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        user = self.request.user
        return Book.objects.filter(user=user)

    def post(self, request, *args, **kwargs):
        kwargs["user"] = self.request.user
        super().post(request, *args, **kwargs)


@method_decorator(login_required(login_url="/"), 'get')
@method_decorator(login_required(login_url="/"), 'patch')
@method_decorator(login_required(login_url="/"), 'put')
@method_decorator(login_required(login_url="/"), 'delete')
class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)
