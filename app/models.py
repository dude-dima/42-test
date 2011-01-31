from django.db import models


class Customer(models.Model):
    """Customer"""
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    contacts = models.CharField(max_length=15)
    bio = models.TextField(max_length=250)

    class Meta:
        db_table = 'users'

    def __unicode__(self):
        return self.name


class Request(models.Model):
    """Request"""
    date = models.DateTimeField(null=True, blank=True, auto_now=True)
    request = models.TextField()

    class Meta:
        db_table = 'requests'
