import time
from functools import wraps
from typing import Any, Callable

from django.conf import settings
from django.contrib.auth.models import Permission
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

from common.helpers import getLogger

logger = getLogger(__name__)

def permission_required(permission:Permission) -> Callable:
    def _decorator(func):
        def __w(request:HttpRequest, *args, **kw):
            user = request.user
            if user.has_perm(permission):
                return func(request, *args, **kw)
            return HttpResponse('Forbidden', status=403)

        return __w

    return _decorator

def retry_on() -> Callable:
    def _retry(func):
        @wraps(func)
        async def inner(*args, **kwargs):
            max_retry = kwargs.pop('max_retry', 1)
            max_retry = max_retry
            retry = 0

            while True:
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    if retry < max_retry:
                        logger.warning('%s, proceed to retry.', e)
                        retry += 1
                        time.sleep(1)
                        continue
                    else:
                        # logger.error(
                        #     'After %s retries still got %s, give up.',
                        #     retry, e, exc_info=True)
                        raise e

        return inner

    return _retry
