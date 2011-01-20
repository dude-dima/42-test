from django.db import models


class Customer(models.Model):
    """Customer"""
    name = models.CharField(null=True, blank=True, max_length=250)
    surname = models.CharField(null=True, blank=True, max_length=250)
    bio = models.TextField(null=True, blank=True, max_length=250)
    contacts = models.TextField(null=True, blank=True, max_length=250)

    def __unicode__(self):
        return self.name    

    class Meta:
        db_table = 'users'
        
    def get_data(self):
        return [(field.name, field.value_to_string(self)) \
                for field in self._meta.fields]
