# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from artigo_app import facade
from routes.artigos import admin


@no_csrf
def index(artigo_id):
    artigo = facade.get_artigo_cmd(artigo_id)()
    detail_form = facade.artigo_detail_form()
    context = {'save_path': router.to_path(save, artigo_id), 'artigo': detail_form.fill_with_model(artigo)}
    return TemplateResponse(context, 'artigos/admin/form.html')


def save(_handler, artigo_id, **artigo_properties):
    cmd = facade.update_artigo_cmd(artigo_id, **artigo_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'artigo': cmd.form}

        return TemplateResponse(context, 'artigos/admin/form.html')
    _handler.redirect(router.to_path(admin))

