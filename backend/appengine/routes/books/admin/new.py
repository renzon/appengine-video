# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from book_app import facade
from routes.books import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'books/admin/form.html')


def save(_handler, book_id=None, **book_properties):
    cmd = facade.save_book_cmd(**book_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'book': cmd.form}

        return TemplateResponse(context, 'books/admin/form.html')
    _handler.redirect(router.to_path(admin))

