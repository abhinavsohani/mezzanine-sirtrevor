mezzanine-sirtrevor
=========

[Sir Trevor editor] for [Mezzanine CMS]. It replaces the default editor with [Sir Trevor editor] . The code is taken from [django-sirtrevor] and made the appropriate changes to work with mezzanine and incorporate media library with image upload.

Quick start
-----------

1. Install mezzanine-sirtrevor::

    > pip install mezzanine-sirtrevor

2. Add ``sirtrevor`` to your INSTALLED_APPS setting like this::

    > INSTALLED_APPS = (
    >
    >   'sirtrevor'.
    >    .....
    > )

3. Add sirtrevor urls::

    > url(r'^sirtrevor/', include('sirtrevor.urls')),
4. add below settings
   
   > RICHTEXT_WIDGET_CLASS = "sirtrevor.widgets.SirTrevorWidget"
   
   > RICHTEXT_FILTERS = (
     "sirtrevor.filters.json_html",
)   



-------
**that's it. now you can see new editor in admin and inline editing area.**

Limitation
------------
"sirtrevor" should be the first app in your installed apps list because it overrides editable.js. If you have your custom theme app then unfortunate you need to merge your app with sirtrevor app.


Configuration
-------------
``SIRTREVOR_UPLOAD_PATH``
   Path where to store uploaded images relative to MEDIA_ROOT. (not configurable via widget kwargs) Defaults to uploads 

Please check [Sir Trevor editor] and [django-sirtrevor] for more configuration options.


[Mezzanine CMS]:http://mezzanine.jupo.org/
[Sir Trevor editor]:http://madebymany.github.io/sir-trevor-js/
[django-sirtrevor]:https://github.com/philippbosch/django-sirtrevor
[configuration options]:http://madebymany.github.io/sir-trevor-js/docs.html#2


    