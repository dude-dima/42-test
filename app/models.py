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
