mezzanine-sirtrevor
===================
Replaces defualt rich text widget wiht 
Provides rich text widgets and filters for Mezzanine based on awesome `Sir Trevor editor`_. I reused most of the code of `django-sirtrevor`_.

Quick start
-----------

1. Add `mezzanine_sirtrevor` to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'mezzanine_sirtrevor',
    )


   - add  ``RICHTEXT_WIDGET_CLASS = "mezzanine_sirtrevor.widgets.SirTrevorWidget"``
   - add  ``RICHTEXT_FILTER = "mezzanine_sirtrevor.filters.json_html"``


Configuration
-------------

`Sir Trevor` has a few `configuration options`_. You can customize most of them 
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

.. _Sir Trevor editor: http://madebymany.github.io/sir-trevor-js/
.. _django-sirtrevor: https://github.com/philippbosch/django-sirtrevor
.. _configuration options: http://madebymany.github.io/sir-trevor-js/docs.html#2	
	
	