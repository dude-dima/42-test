from django.db import models


class Customer(models.Model):
    """Customer"""
    name = models.CharField(null=True, max_length=15)
    surname = models.CharField(null=True, max_length=15)
    contacts = models.CharField(null=True, max_length=15)
    bio = models.TextField(null=True, max_length=250)
    birth_date = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    def get_data(self):
        return [(field.name, field.value_to_string(self))\
                for field in self._meta.fields]

    class Meta:
        db_table = 'users'


class Request(models.Model):
    """Request"""
    date = models.DateTimeField(null=True, blank=True, auto_now=True)
    request = models.TextField()

    class Meta:
        db_table = 'requests'
