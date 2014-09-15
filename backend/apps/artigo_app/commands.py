# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from artigo_app.model import Artigo

class ArtigoPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Artigo
    _include = [Artigo.titulo, 
                Artigo.publicacao]


class ArtigoForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Artigo
    _include = [Artigo.titulo, 
                Artigo.publicacao]


class ArtigoDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Artigo
    _include = [Artigo.titulo, 
                Artigo.creation, 
                Artigo.publicacao]


class ArtigoShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Artigo
    _include = [Artigo.titulo, 
                Artigo.creation, 
                Artigo.publicacao]


class SaveArtigoCommand(SaveCommand):
    _model_form_class = ArtigoForm


class UpdateArtigoCommand(UpdateNode):
    _model_form_class = ArtigoForm


class ListArtigoCommand(ModelSearchCommand):
    def __init__(self):
        super(ListArtigoCommand, self).__init__(Artigo.query_by_creation())

