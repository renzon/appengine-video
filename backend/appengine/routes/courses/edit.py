# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from course_app import course_facade
from routes import courses
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index(course_id):
    course = course_facade.get_course_cmd(course_id)()
    course_form = course_facade.course_form()
    context = {'save_path': router.to_path(save, course_id), 'course': course_form.fill_with_model(course)}
    return TemplateResponse(context, 'courses/course_form.html')


def save(course_id, **course_properties):
    cmd = course_facade.update_course_cmd(course_id, **course_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors, 'course': course_properties}

        return TemplateResponse(context, 'courses/course_form.html')
    return RedirectResponse(router.to_path(courses))

