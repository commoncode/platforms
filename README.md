Platforms
=========

Multi-site platform resolution for Django


## Code

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


## Platform Resolutions


    platform = Platform.objects.get(slug='commoncode')
    resolutions = Resolution.objects.filter(platform=platform)
    print resolutions
    >>> ['commoncode.io', 'commoncode.com.au' ]

    # resolve the following Resolutions inbound by
    # request.get_path()

    path = request.get_path()
    print path
    >>> http://commoncode.io/some/url/

    resolution = get_resolution(path)
    print resolution.platform
    >>> commoncode

