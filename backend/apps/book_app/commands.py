# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from book_app.model import Book

class BookPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Book
    _include = [Book.edition, 
                Book.price, 
                Book.title]


class BookForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Book
    _include = [Book.edition, 
                Book.price, 
                Book.title]


class BookDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Book
    _include = [Book.edition, 
                Book.price, 
                Book.creation, 
                Book.title]


class BookShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Book
    _include = [Book.edition, 
                Book.price, 
                Book.creation, 
                Book.title]


class SaveBookCommand(SaveCommand):
    _model_form_class = BookForm


class UpdateBookCommand(UpdateNode):
    _model_form_class = BookForm


class ListBookCommand(ModelSearchCommand):
    def __init__(self):
        super(ListBookCommand, self).__init__(Book.query_by_creation())

