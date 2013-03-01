# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger(__name__)

from django.conf import settings
from django.core.exceptions import MiddlewareNotUsed


class PlatformResolutionMiddleware(object):
    """Given a request, resolve the Platform.
    """
    def __init__(self):
        """This middleware must be enabled, as well as included in
        MIDDLEWARE_CLASSES
        """
        if not getattr(settings, 'PLATFORMS_USE_PLATFORMS', False):
            logger.debug('PLATFORMS_USE_PLATFORMS setting must be True to use this middleware')
            raise MiddlewareNotUsed

    def process_request(self, request):
        logger.debug('PlatformResolutionMiddleware.process_request entered')
        return None

    # will other methods be useful? process_view,
    # process_template_response, process_response, process_exception
