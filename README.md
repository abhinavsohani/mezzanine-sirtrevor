mezzanine-sirtrevor
=========

Replaces defualt rich text widget of [Mezzanine CMS] based on awesome [Sir Trevor editor]. I reused most of the code of [django-sirtrevor].

** warning:-**
============
not ready to use in prduciton. image upload is not yet implemented.
Quick start
=========
-----------------------
- Add `mezzanine_sirtrevor` to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'mezzanine_sirtrevor',
    )


 
   - add  ``RICHTEXT_WIDGET_CLASS = "mezzanine_sirtrevor.widgets.SirTrevorWidget"``
   - add  ``RICHTEXT_FILTER = "mezzanine_sirtrevor.filters.json_html"``
-------
**that's it. now you can see new editor in admin and inline editing area.**

Configuration
-------------

`Sir Trevor` has a few [configuration options]. You can customize most of them 
project-wide in your ``settings.py`` or on a per-widget basis as ``kwargs`` for 
``SirTrevorWidget``.

**Available options** (``CONFIGURATION_SETTINGS`` / ``widget_kwargs``):


``SIRTREVOR_BLOCK_TYPES`` / ``st_block_types``
    Specify an array of block types to use with the editor.
    Defaults to ``['Text', 'List', 'Quote', 'Image', 'Video', 'Tweet', 'Heading']``

``SIRTREVOR_DEFAULT_TYPE`` / ``st_default_type``
    Specify a default block to start the editor with.
    Defaults to ``None``

``SIRTREVOR_BLOCK_LIMIT`` / ``st_block_limit``
    Set an overall total number of blocks that can be displayed.
    Defaults to ``0``

``SIRTREVOR_BLOCK_TYPE_LIMITS`` / ``st_block_type_limits``
    Set a limit on the number of blocks that can be displayed by its type.
    Defaults to ``{}``

``SIRTREVOR_REQUIRED`` / ``st_required``
    Specify which block types are required for validatation.
    Defaults to ``None``




[Mezzanine CMS]:http://mezzanine.jupo.org/
[Sir Trevor editor]:http://madebymany.github.io/sir-trevor-js/
[django-sirtrevor]:https://github.com/philippbosch/django-sirtrevor
[configuration options]:http://madebymany.github.io/sir-trevor-js/docs.html#2


    