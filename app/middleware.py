from app.models import Request


class RequestHandler:
    """Handles each request"""

    def process_request(self, request):
        req = Request(request=request)
        if request.user.is_authenticated():
            req.priority = 1
        req.save()
        return None
