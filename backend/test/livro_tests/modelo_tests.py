# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from datetime import date

from base import GAETestCase
from livro_app.modelo import Book
from mommygae import mommy


class BookTests(GAETestCase):
    def test_salvar_livro(self):
        livro = mommy.make_one(Book, title='App Engine e Python')
        livro.put()
        livros_em_bd = livro.query_by_creation().fetch()
        self.assertListEqual([livro], livros_em_bd)
        self.assertEqual('App Engine e Python', livros_em_bd[0].title)