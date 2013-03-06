
class PlatformListMixin(object):
    """ Override get_queryset to make use of platforms if it is
    installed to filter the results
    """
    def get_queryset(self):
        if hasattr(self.model.objects, "platform"):
            return self.model.objects.platform(self.request.platform)
        else:
            return super(PlatformListMixin, self).get_queryset()


class PlatformDetailMixin(object):
    """ Override get_queryset to make use of platforms if it is
    installed to filter the results
    """
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if hasattr(self.model.objects, "platform") and slug:        
            return self.model.objects.platform(self.request.platform).filter(
                slug=slug
            )
        else:
            return super(PlatformDetailMixin, self).get_queryset()