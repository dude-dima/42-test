from django.db.models.signals import post_save, post_delete
from app.models import Request, Customer, LogModel


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
