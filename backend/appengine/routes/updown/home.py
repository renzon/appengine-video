# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import logging
from google.appengine.api.app_identity.app_identity import get_default_gcs_bucket_name
from google.appengine.ext.blobstore import blobstore
from blob_app import blob_facade
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from tekton import router
from routes.updown import upload, download
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index(_logged_user):
    """
    This is a example of file upload using
    Google Cloud Storage
    :return:
    """
    success_url = router.to_path(upload)
    bucket = get_default_gcs_bucket_name()
    logging.info(bucket)
    url = blobstore.create_upload_url(success_url, gs_bucket_name=bucket)
    cmd = blob_facade.list_blob_files_cmd(_logged_user)
    blob_form = blob_facade.blob_file_form()
    deletar_path_base = router.to_path(delete)
    download_path_base = router.to_path(download)

    def localizar_blob(blob):
        dct = blob_form.fill_with_model(blob, 64)
        dct['delete_path'] = router.to_path(deletar_path_base, dct['id'])
        dct['download_path'] = router.to_path(download_path_base, blob.blob_key, dct['filename'].encode('utf8'))
        return dct

    blob_files = [localizar_blob(b) for b in cmd()]
    context = {'upload_url': url,
               'blob_files': blob_files}
    return TemplateResponse(context, 'updown/home.html')


def delete(blob_chave):
    cmd = blob_facade.delete_blob_file_cmd(blob_chave)
    cmd.execute()
    return RedirectResponse(index)