from django.db import models


class Customer(models.Model):
    """Customer"""
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    bio = models.TextField(max_length=250)
    contacts = models.TextField(max_length=250)

    class Meta:
        db_table = 'users'

    def __unicode__(self):
        return self.name

    def get_data(self):
        return [(field.name, field.value_to_string(self)) \
                for field in self._meta.fields]
