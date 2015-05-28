# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from course_app.course_model import Course
from mommygae import mommy
from routes.courses import home


class IndexTests(GAETestCase):
    def test_index(self):
        mommy.save_one(Course)
        resposta = home.index()
        self.assert_can_render(resposta)

