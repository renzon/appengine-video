# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from datetime import date
from base import GAETestCase
from livro_app.modelo import Book


class BookTests(GAETestCase):
    def test_salvar_livro(self):
        livro = Book(title='App Engine e Python', price=39.99, release=date(2014, 9, 2))
        livro.put()
        livros_em_bd = livro.query_by_creation().fetch()
        self.assertListEqual([livro], livros_em_bd)