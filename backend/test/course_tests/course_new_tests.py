# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from datetime import datetime, date
from decimal import Decimal
from course_app.course_model import Course
from routes.courses.new import index, save
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        template_response = index()
        self.assert_can_render(template_response)


class SaveTests(GAETestCase):
    def test_success(self):
        self.assertIsNone(Course.query().get())
        redirect_response = save(nome='nome_string')
        self.assertIsInstance(redirect_response, RedirectResponse)
        saved_course = Course.query().get()
        self.assertIsNotNone(saved_course)
        self.assertEquals('nome_string', saved_course.nome)

    def test_error(self):
        template_response = save()
        errors = template_response.context['errors']
        self.assertSetEqual(set(['nome']), set(errors.keys()))
        self.assert_can_render(template_response)
