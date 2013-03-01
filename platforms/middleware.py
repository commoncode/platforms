# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.exceptions import MiddlewareNotUsed


class PlatformResolutionMiddleware(object):
    """Given a request, resolve the Platform.
    """
    def __init__(self):
        """This middleware must be enabled, as well as included in
        INSTALLED_MIDDLEWARE"""

        if not getattr(settings, 'PLATFORMS_USE_PLATFORMS', False):
            raise MiddlewareNotUsed

    def process_request(self, request):
        return None

    # will other methods be useful? process_view,
    # process_template_response, process_response, process_exception
