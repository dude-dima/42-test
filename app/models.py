from django.db import models
from django.db.models.signals import post_save, post_delete


class Customer(models.Model):
    """Customer"""
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    contacts = models.CharField(max_length=15)
    bio = models.TextField(max_length=250)
    birth_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'users'

    def __unicode__(self):
        return self.name


class Request(models.Model):
    """Request"""
    date = models.DateTimeField(auto_now=True)
    request = models.TextField()
    priority = models.IntegerField(default=0)

    class Meta:
        db_table = 'requests'


class LogModel(models.Model):
    """Logs every model changing, creation, deletion"""
    date = models.DateTimeField(auto_now=True)
    model = models.CharField(max_length=50)
    action = models.CharField(max_length=15)

    class Meta:
        db_table = 'model_logs'


def log(sender, **kwargs):
    if sender not in (Request, Customer):
        return
    log_model = LogModel(model=str(sender))
    if 'created' in kwargs:
        log_model.action = ('Created', 'Changed')[int(kwargs['created'])]
    else:
        log_model.action = "Deleted"
    log_model.save()


post_save.connect(log)
post_delete.connect(log)
