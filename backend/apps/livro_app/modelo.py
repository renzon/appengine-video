# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node, Arc


class Book(Node):
    title = ndb.StringProperty(required=True)
    price = ndb.FloatProperty()

    release = ndb.DateProperty()


class AutorArco(Arc):
    origin = ndb.KeyProperty(required=True)
    destination = ndb.KeyProperty(Book, required=True)