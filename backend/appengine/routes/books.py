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
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index():
    query = Book.query().order(-Book.price)
    livro_lista = query.fetch()
    book_form = BookFormTable()
    livro_lista = [book_form.fill_with_model(livro) for livro in livro_lista]
    editar_form_path = router.to_path(editar_form)
    delete_path = router.to_path(delete)
    for livro in livro_lista:
        livro['edit_path'] = '%s/%s' % (editar_form_path, livro['id'])
        livro['delete_path'] = '%s/%s' % (delete_path, livro['id'])
    contexto = {'livro_lista': livro_lista,
                'form_path':router.to_path(form)}
    return TemplateResponse(contexto)

def delete(book_id):
    chave=ndb.Key(Book,int(book_id))
    chave.delete()
    return RedirectResponse(router.to_path(index))


@no_csrf
def editar_form(book_id):
    book_id = int(book_id)
    book = Book.get_by_id(book_id)
    book_form = BookForm()
    book_form.fill_with_model(book)
    contexto = {'salvar_path': router.to_path(editar, book_id),
                'book': book_form}
    return TemplateResponse(contexto, 'books/form.html')


def editar(book_id, **propriedades):
    book_id = int(book_id)
    book = Book.get_by_id(book_id)
    book_form = BookForm(**propriedades)
    erros = book_form.validate()
    if erros:
        contexto = {'salvar_path': router.to_path(salvar),
                    'erros': erros,
                    'book': book_form}
        return TemplateResponse(contexto, 'books/form.html')
    else:
        book_form.fill_model(book)
        book.put()
        return RedirectResponse(router.to_path(index))


@no_csrf
def form():
    contexto = {'salvar_path': router.to_path(salvar)}
    return TemplateResponse(contexto)


class Book(Node):
    title = ndb.StringProperty(required=True)
    price = ndb.FloatProperty()
    release = ndb.DateProperty()


class BookFormTable(ModelForm):
    _model_class = Book
    _include = [Book.title, Book.creation, Book.price]


class BookForm(ModelForm):
    _model_class = Book
    _include = [Book.title, Book.release, Book.price]


def salvar(**propriedades):
    book_form = BookForm(**propriedades)
    erros = book_form.validate()
    if erros:
        contexto = {'salvar_path': router.to_path(salvar),
                    'erros': erros,
                    'book': book_form}
        return TemplateResponse(contexto, 'books/form.html')
    else:
        book = book_form.fill_model()
        book.put()
        return RedirectResponse(router.to_path(index))