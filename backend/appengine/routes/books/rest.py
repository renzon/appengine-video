# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from book_app import facade


def index():
    cmd = facade.list_books_cmd()
    book_list = cmd()
    short_form=facade.book_short_form()
    book_short = [short_form.fill_with_model(m) for m in book_list]
    return JsonResponse(book_short)


def save(**book_properties):
    cmd = facade.save_book_cmd(**book_properties)
    return _save_or_update_json_response(cmd)


def update(book_id, **book_properties):
    cmd = facade.update_book_cmd(book_id, **book_properties)
    return _save_or_update_json_response(cmd)


def delete(book_id):
    facade.delete_book_cmd(book_id)()


def _save_or_update_json_response(cmd):
    try:
        book = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.book_short_form()
    return JsonResponse(short_form.fill_with_model(book))

