from django import http

from django.shortcuts import render_to_response
from mezzanine.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.dispatch import Signal
from json import dumps
import os
import re
from django.core.urlresolvers import reverse
from filebrowser_safe.settings import *
from filebrowser_safe.functions import (get_path, get_breadcrumbs,
    get_filterdate, get_settings_var, get_directory, convert_filename)
from django.core.files.storage import default_storage
from filebrowser_safe.base import FileObject	
try:
    from django.utils.encoding import smart_text
except ImportError:
    # Backward compatibility for Py2 and Django < 1.5
    from django.utils.encoding import smart_unicode as smart_text
# upload signals
filebrowser_pre_upload = Signal(providing_args=["path", "file"])
filebrowser_post_upload = Signal(providing_args=["path", "file"])
@csrf_exempt

def _upload_file_sir(request):
    """
    Upload file to the server.

    Implement unicode handlers - https://github.com/sehmaschine/django-filebrowser/blob/master/filebrowser/sites.py#L471
    """
    if request.method == 'POST':
        folder = request.POST.get('folder')
        fb_uploadurl_re = re.compile(r'^.*(%s)' % reverse("fb_upload"))
        folder = fb_uploadurl_re.sub('', folder)

        if request.FILES:
            filedata = request.FILES['Filedata']
            # PRE UPLOAD SIGNAL
            filebrowser_pre_upload.send(sender=request, path=request.POST.get('folder'), file=filedata)

            filedata.name = convert_filename(filedata.name)

            # HANDLE UPLOAD
            exists = default_storage.exists(os.path.join(get_directory(), folder, filedata.name))
            abs_path = os.path.join(get_directory(), folder, filedata.name)
            uploadedfile = default_storage.save(abs_path, filedata)

            path = os.path.join(get_directory(), folder)
            file_name = os.path.join(path, filedata.name)
            if exists:
                default_storage.move(smart_text(uploadedfile), smart_text(file_name), allow_overwrite=True)
            
            # POST UPLOAD SIGNAL
            filebrowser_post_upload.send(sender=request, path=request.POST.get('folder'), file=FileObject(smart_text(file_name)))
            response_data = {}
            response_data['url'] = uploadedfile
            response_data['default_url'] = uploadedfile
    return HttpResponse(dumps(response_data), content_type="application/json")