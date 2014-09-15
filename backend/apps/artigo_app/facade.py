# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from artigo_app.commands import ListArtigoCommand, SaveArtigoCommand, UpdateArtigoCommand, \
    ArtigoPublicForm, ArtigoDetailForm, ArtigoShortForm


def save_artigo_cmd(**artigo_properties):
    """
    Command to save Artigo entity
    :param artigo_properties: a dict of properties to save on model
    :return: a Command that save Artigo, validating and localizing properties received as strings
    """
    return SaveArtigoCommand(**artigo_properties)


def update_artigo_cmd(artigo_id, **artigo_properties):
    """
    Command to update Artigo entity with id equals 'artigo_id'
    :param artigo_properties: a dict of properties to update model
    :return: a Command that update Artigo, validating and localizing properties received as strings
    """
    return UpdateArtigoCommand(artigo_id, **artigo_properties)


def list_artigos_cmd():
    """
    Command to list Artigo entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListArtigoCommand()


def artigo_detail_form(**kwargs):
    """
    Function to get Artigo's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return ArtigoDetailForm(**kwargs)


def artigo_short_form(**kwargs):
    """
    Function to get Artigo's short form. just a subset of artigo's properties
    :param kwargs: form properties
    :return: Form
    """
    return ArtigoShortForm(**kwargs)

def artigo_public_form(**kwargs):
    """
    Function to get Artigo'spublic form. just a subset of artigo's properties
    :param kwargs: form properties
    :return: Form
    """
    return ArtigoPublicForm(**kwargs)


def get_artigo_cmd(artigo_id):
    """
    Find artigo by her id
    :param artigo_id: the artigo id
    :return: Command
    """
    return NodeSearch(artigo_id)


def delete_artigo_cmd(artigo_id):
    """
    Construct a command to delete a Artigo
    :param artigo_id: artigo's id
    :return: Command
    """
    return DeleteNode(artigo_id)

