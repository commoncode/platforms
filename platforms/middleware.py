# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger(__name__)

import re

from django.conf import settings
from django.core.exceptions import MiddlewareNotUsed

from .models import Resolution


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
        request.platform = None
        try:
            http_host = request.META['HTTP_HOST']
        except KeyError:
            logger.error('No Host header in request, cannot resolve Platform')
            return None

        #
        ## TODO, the algorithm for resolving to a single Platform is TBD.
        #

        # 1. Hostname–only Platform Resolution
        try:
            hostonly_res = Resolution.objects.filter(domain__endswith=http_host,
                                                     uripattern='')[0]
            logger.debug('Host-only Resolution: {}'.format(hostonly_res))
            logger.debug('Platform is {}'.format(hostonly_res.platform))
            request.platform = hostonly_res.platform
            return None
        except IndexError:
            logger.debug('No hostname-only Resolution for {}'.format(http_host))

        # 2. URI path regex testing, first to match wins
        simple_res = Resolution.objects.filter(domain__endswith=http_host,
                                               uripattern__isnull=False)
        logger.debug(simple_res)
        for res in simple_res:
            logger.debug('Resolution: {} URI Pattern: {}'.format(res, res.uripattern))
            if re.match(res.uripattern, request.path):
                logger.debug('Platform is {}'.format(res.platform))
                request.platform = res.platform
                return None
        return None

    # will other methods be useful? process_view,
    # process_template_response, process_response, process_exception
