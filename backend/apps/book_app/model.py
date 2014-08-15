# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node
from gaeforms.ndb import property


class Book(Node):
    price = property.SimpleCurrency(required=True)
    title = ndb.StringProperty(required=True)
    edition = ndb.DateProperty(required=True)

