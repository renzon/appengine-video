# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node
from gaeforms.ndb import property

NOVA = 'NOVA'
CONTABILIZADA = 'CONTABILIZADA'

LISTA_DE_STATUS = [NOVA, CONTABILIZADA]


class Venda(Node):
    preco = property.SimpleCurrency(required=True)
    status = ndb.StringProperty(required=True, choices=LISTA_DE_STATUS, default=NOVA)

    @classmethod
    def query_by_stats_order_by_creation(cls, status):
        return cls.query(cls.status == status).order(cls.creation)

