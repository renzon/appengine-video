# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaecookie.decorator import no_csrf


@no_csrf
def index(_handler, _resp, blob_key, filename):
    _handler.send_blob(blob_key)
    header_value = 'attachment; filename=%s' % filename
    _resp.headers.add('Content-Disposition'.encode('utf8'), header_value.encode('utf8'))