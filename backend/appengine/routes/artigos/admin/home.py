# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from artigo_app import facade
from routes.artigos.admin import new, edit


def delete(_handler, artigo_id):
    facade.delete_artigo_cmd(artigo_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_artigos_cmd()
    artigos = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.artigo_short_form()

    def short_artigo_dict(artigo):
        artigo_dct = short_form.fill_with_model(artigo)
        artigo_dct['edit_path'] = router.to_path(edit_path, artigo_dct['id'])
        artigo_dct['delete_path'] = router.to_path(delete_path, artigo_dct['id'])
        return artigo_dct

    short_artigos = [short_artigo_dict(artigo) for artigo in artigos]
    context = {'artigos': short_artigos,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

