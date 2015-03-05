# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import unittest


def soma(parcela, parcela2):
    pass


class ExemploTests(unittest.TestCase):
    def test_soma(self):
        resultado = soma(1, 2)
        self.assertEqual(4, resultado)

    def test_blah(self):
        pass