mezzanine-sirtrevor
=========

Provides awesome [Sir Trevor editor] for [Mezzanine CMS] based Most of the code is taken from [django-sirtrevor] and made the appropriate changes to incorporate media library with image upload.

Quick start
-----------

1. Install django-sirtrevor::

    pip install mezzanine-sirtrevor

2. Add ``sirtrevor`` to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'sirtrevor',
    )

3. Add sir trevor urls::

    url(r'^sirtrevor/', include('sirtrevor.urls')),
   
-------
**that's it. now you can see new editor in admin and inline editing area.**

Configuration
-------------
``SIRTREVOR_UPLOAD_PATH``
   Path where to store uploaded images relative to MEDIA_ROOT. (not configurable via widget kwargs) Defaults to uploads 

Please check [Sir Trevor editor] and [django-sirtrevor] for more configuration options.


[Mezzanine CMS]:http://mezzanine.jupo.org/
[Sir Trevor editor]:http://madebymany.github.io/sir-trevor-js/
[django-sirtrevor]:https://github.com/philippbosch/django-sirtrevor
[configuration options]:http://madebymany.github.io/sir-trevor-js/docs.html#2


    