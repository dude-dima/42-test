def add_settings(request):
    from django.conf import settings
    return {'settings': settings}
