from entropy.base import TitleMixin, SlugMixin

from django.db import models


class Platform(TitleMixin, SlugMixin):
    # title and short_title from TitleMixin
    # slug from SlugMixin
    pass
