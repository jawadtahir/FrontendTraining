from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Name (models.Model):
    _salutation_option = (
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Dr', 'Dr'),
        ('Prof', 'Prof')
    )
    salutation = models.CharField(
        max_length=10, choices=_salutation_option, blank=True
    )
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)

    class Meta:
        db_table = "Name"

    def __str__(self):
        return self.salutation.join(" ") if self.salutation else "" + \
                                                                 "%s %s" % \
                                                                 (self.first_name,
                                                                  self.last_name
                                                                  )

    @classmethod
    def get_salutations(cls):
        return cls._salutation_option


class Author(models.Model):
    name = models.OneToOneField(Name, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True)

    class Meta:
        db_table = "Author"

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.OneToOneField(Name, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    country = models.CharField(max_length=30)

    class Meta:
        db_table = "Publisher"

    def __str__(self):
        return "%s of %s" % (self.name, self.country)


class Contact(models.Model):
    _contact_method_options = (
        ("HP", "Home Phone"),
        ("OP", "Office Phone"),
        ("MP", "Mobile Phone")
    )
    country_code = models.IntegerField(blank=True, null=True)
    carrier_code = models.IntegerField()
    contact_number = models.IntegerField()
    contact_method = models.CharField(
        max_length=2, choices=_contact_method_options
    )
    active = models.BinaryField(default=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    publisher = models.ForeignKey(
        Publisher, on_delete=models.CASCADE, null=True
    )

    class Meta:
        db_table = "Contact"

    def get_contact_method_option(self):
        return self._contact_method_options

    def __str__(self):
        return (
            "+".join(self.country_code.__str__())
            if self.country_code else "0").join(
            self.carrier_code.__str__()).join(self.contact_number.__str__())


class Book(models.Model):
    name = models.TextField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    user = models.ForeignKey(User)

    class Meta:
        db_table = "Book"

    def __str__(self):
        return "%s by %s" % (self.name, self.authors.first())
