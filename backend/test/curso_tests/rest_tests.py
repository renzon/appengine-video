# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from course_app.course_model import Course
from mommygae import mommy
from routes.courses import rest


class ListarTests(GAETestCase):
    def test_sucesso(self):
        mommy.save_one(Course)
        resposta = rest.index()
        self.assert_can_serialize_as_json(resposta)