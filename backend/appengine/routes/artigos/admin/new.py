# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from artigo_app import facade
from routes.artigos import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'artigos/admin/form.html')


def save(_handler, artigo_id=None, **artigo_properties):
    cmd = facade.save_artigo_cmd(**artigo_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'artigo': cmd.form}

        return TemplateResponse(context, 'artigos/admin/form.html')
    _handler.redirect(router.to_path(admin))

