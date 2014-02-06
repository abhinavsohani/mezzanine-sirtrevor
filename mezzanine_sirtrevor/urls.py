from __future__ import unicode_literals
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns("",
    
	url(r'^attachmentss/$', 'mezzanine_sirtrevor.views._upload_file_sir', name="fb_browsse"),
	
)

# Adds ``STATIC_URL`` to the context.
handler500 = "mezzanine.core.views.server_error"
