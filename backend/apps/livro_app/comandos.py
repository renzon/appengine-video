# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, UpdateCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import DestinationsSearch, CreateArc, DeleteArcs
from livro_app.modelo import Book, AutorArco


class BookFormTable(ModelForm):
    _model_class = Book
    _include = [Book.title, Book.creation, Book.price]


class BookForm(ModelForm):
    _model_class = Book
    _include = [Book.title, Book.release, Book.price]


# Comandos

class ListarLivrosDeAutor(DestinationsSearch):
    def __init__(self, autor):
        super(ListarLivrosDeAutor, self).__init__(AutorArco, autor)


class SalvarLivroComAutor(CreateArc):
    def __init__(self, autor, **propriedades_do_livro):
        salvar_livro_cmd = SalvarLivro(**propriedades_do_livro)
        super(SalvarLivroComAutor, self).__init__(AutorArco, autor, salvar_livro_cmd)


class SalvarLivro(SaveCommand):
    _model_form_class = BookForm


class EditarLivro(UpdateCommand):
    _model_form_class = BookForm


class ApagarAutorArcos(DeleteArcs):
    def __init__(self, livro):
        super(ApagarAutorArcos, self).__init__(AutorArco, destination=livro)