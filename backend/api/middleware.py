from .models import GetRequestActivityLog
import logging

logger = logging.getLogger(__name__)


class GetRequestLogger:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        try:
            if request.method == 'GET':
                get_log = GetRequestActivityLog.objects.create(method=request.method, url=request.path)
                get_log.save()
        except Exception:
            logger.debug(f'method={request.method} path={request.path}')

        return response
