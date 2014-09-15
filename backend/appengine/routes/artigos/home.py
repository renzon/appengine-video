# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from artigo_app import facade
from routes.artigos import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_artigos_cmd()
    artigos = cmd()
    public_form = facade.artigo_public_form()
    artigo_public_dcts = [public_form.fill_with_model(artigo) for artigo in artigos]
    context = {'artigos': artigo_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

