# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from artigo_app import facade


def index():
    cmd = facade.list_artigos_cmd()
    artigo_list = cmd()
    short_form=facade.artigo_short_form()
    artigo_short = [short_form.fill_with_model(m) for m in artigo_list]
    return JsonResponse(artigo_short)


def save(**artigo_properties):
    cmd = facade.save_artigo_cmd(**artigo_properties)
    return _save_or_update_json_response(cmd)


def update(artigo_id, **artigo_properties):
    cmd = facade.update_artigo_cmd(artigo_id, **artigo_properties)
    return _save_or_update_json_response(cmd)


def delete(artigo_id):
    facade.delete_artigo_cmd(artigo_id)()


def _save_or_update_json_response(cmd):
    try:
        artigo = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.artigo_short_form()
    return JsonResponse(short_form.fill_with_model(artigo))

