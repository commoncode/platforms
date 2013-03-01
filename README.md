Platforms
=========

A Django app to do *multi-site platform resolution*.

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

## Front–end web server config.

Catch–all vhost config. which sends all incoming requests to a single *upstream* Django socket.

The `Host` header of the proxied request is used in the *Platform* resolution process, along with the URI.

## Setup

+ Add to `INSTALLED_APPS`
+ Add to `MIDDLEWARE`
+ Set `PLATFORMS_USE_PLATFORMS = True`

## Platform Resolutions

    >>> platform = Platform.objects.get(slug='commoncode')
    >>> resolutions = Resolution.objects.filter(platform=platform)
    >>> print resolutions
    ['commoncode.io', 'commoncode.com.au' ]

    # resolve the following Resolutions inbound by
    # request.get_path()

    >> path = request.get_path()
    >>> print path
    http://commoncode.io/some/url/

    >>> resolution = get_resolution(path)
    >>> print resolution.platform
    commoncode

