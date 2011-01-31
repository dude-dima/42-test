from models import Request


class RequestHandler:
    """Handles each request"""

    def process_request(self, request):
        Request.objects.create(request=request)
        return None
