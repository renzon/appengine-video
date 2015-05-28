# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from config.template_middleware import TemplateResponse
from course_app.course_model import Course
from routes.courses import new
from tekton.gae.middleware.redirect import RedirectResponse


class SalvarTests(GAETestCase):
    def test_sucesso(self):
        resposta = new.save(nome='App Engine')
        self.assertIsInstance(resposta, RedirectResponse)
        curso = Course.query().get()
        self.assertIsNotNone(curso)
        self.assertEqual('App Engine', curso.nome)

    def test_falha(self):
        resposta = new.save(nome='')
        self.assertIsInstance(resposta, TemplateResponse)
        self.assert_can_render(resposta)
        self.assertDictEqual({'nome': u'Required field'}, resposta.context['errors'])
