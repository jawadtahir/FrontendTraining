from django.db import models


# Create your models here.
class Name (models.Model):
    _salutation_option = (
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Dr', 'Dr'),
        ('Dr', 'Dr')
    )
    salutation = models.CharField(
        max_length=10, choices=_salutation_option, blank=True
    )
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.salutation.join(" ") if self.salutation else "" + \
                                                                 "%s %s" % \
                                                                 (self.first_name,
                                                                  self.last_name
                                                                  )


class Author(models.Model):
    name = models.ForeignKey(Name)
    date_of_birth = models.DateField(blank=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField(blank=True)
    country = models.CharField(max_length=30)

    def __str__(self):
        return "%s of %s" % (self.name, self.country)


class Contact(models.Model):
    contact_method_options = (
        ("HP", "Home Phone"),
        ("OP", "Office Phone"),
        ("MP", "Mobile Phone")
    )
    country_code = models.IntegerField(blank=True)
    carrier_code = models.IntegerField()
    contact_number = models.IntegerField()
    contact_method = models.CharField(
        max_length=2, choices=contact_method_options
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    publisher = models.ForeignKey(
        Publisher, on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return (
            "+".join(self.country_code.__str__())
            if self.country_code else "0").join(
            self.carrier_code.__str__()).join(self.contact_number.__str__())


class Book(models.Model):
    name = models.TextField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)

    def __str__(self):
        return "%s by %s" % (self.name, self.authors.first())