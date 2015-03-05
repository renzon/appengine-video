# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from datetime import datetime, date
from decimal import Decimal
from course_app.course_model import Course
from routes.courses.edit import index, save
from mommygae import mommy
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        course = mommy.save_one(Course)
        template_response = index(course.key.id())
        self.assert_can_render(template_response)


class EditTests(GAETestCase):
    def test_success(self):
        course = mommy.save_one(Course)
        old_properties = course.to_dict()
        redirect_response = save(course.key.id(), nome='nome_string')
        self.assertIsInstance(redirect_response, RedirectResponse)
        edited_course = course.key.get()
        self.assertEquals('nome_string', edited_course.nome)
        self.assertNotEqual(old_properties, edited_course.to_dict())

    def test_error(self):
        course = mommy.save_one(Course)
        old_properties = course.to_dict()
        template_response = save(course.key.id())
        errors = template_response.context['errors']
        self.assertSetEqual(set(['nome']), set(errors.keys()))
        self.assertEqual(old_properties, course.key.get().to_dict())
        self.assert_can_render(template_response)
