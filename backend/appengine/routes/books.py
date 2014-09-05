# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaeforms import base
from gaeforms.base import Form
from gaeforms.ndb.form import ModelForm
from gaegraph.model import Node
from tekton import router


@no_csrf
def form():
    contexto = {'salvar_path': router.to_path(salvar)}
    return TemplateResponse(contexto)


class Book(Node):
    title = ndb.StringProperty(required=True)
    price = ndb.FloatProperty()
    release = ndb.DateProperty()


class BookForm(ModelForm):
    _model_class = Book
    _include = [Book.title, Book.release, Book.price]


def salvar(_resp, **propriedades):
    book_form = BookForm(**propriedades)
    erros = book_form.validate()
    if erros:
        contexto = {'salvar_path': router.to_path(salvar),
                    'erros': erros,
                    'book':book_form}
        return TemplateResponse(contexto, 'books/form.html')
    else:
        book = book_form.fill_model()
        book.put()
        _resp.write(propriedades)