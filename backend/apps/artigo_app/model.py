# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node
from gaeforms.ndb import property


class Artigo(Node):
    titulo = ndb.StringProperty(required=True)
    publicacao = ndb.DateProperty(required=True)

