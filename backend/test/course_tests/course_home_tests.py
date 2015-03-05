# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from course_app.course_model import Course
from routes.courses.home import index, delete
from gaebusiness.business import CommandExecutionException
from gaegraph.model import Node
from mommygae import mommy
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        mommy.save_one(Course)
        template_response = index()
        self.assert_can_render(template_response)


class DeleteTests(GAETestCase):
    def test_success(self):
        course = mommy.save_one(Course)
        redirect_response = delete(course.key.id())
        self.assertIsInstance(redirect_response, RedirectResponse)
        self.assertIsNone(course.key.get())

    def test_non_course_deletion(self):
        non_course = mommy.save_one(Node)
        self.assertRaises(CommandExecutionException, delete, non_course.key.id())
        self.assertIsNotNone(non_course.key.get())

