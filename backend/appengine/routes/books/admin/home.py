# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from book_app import facade
from routes.books.admin import new, edit


def delete(_handler, book_id):
    facade.delete_book_cmd(book_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_books_cmd()
    books = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.book_short_form()

    def short_book_dict(book):
        book_dct = short_form.fill_with_model(book)
        book_dct['edit_path'] = router.to_path(edit_path, book_dct['id'])
        book_dct['delete_path'] = router.to_path(delete_path, book_dct['id'])
        return book_dct

    short_books = [short_book_dict(book) for book in books]
    context = {'books': short_books,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

