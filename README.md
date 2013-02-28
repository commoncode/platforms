Platforms
=========

Multi-site platform resolution for Django


`models.py`:

    Platform(TitleMixin, SlugMixin)
        # title
        # short_title
        # slug

    Resolution

        domain
        uri_regex

        order
        # is_canonical


`middleware.py`:

    # Resolve the request


`settings.py`

    USE_PLATFORMS = get(settings.PLATFORMS_USE_PLATFORMS, False)


## Setup

+ Add to `INSTALLED_APPS`
+ Add to `MIDDLEWARE`
+ Set `PLATFORMS_USE_PLATFORMS = True`
