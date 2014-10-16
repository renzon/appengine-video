# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from config.template_middleware import TemplateResponse
from gaepermission.decorator import login_required
from tekton import router
from gaecookie.decorator import no_csrf
from course_app import course_facade
from routes.courses import new, edit, rest
from tekton.gae.middleware.redirect import RedirectResponse

@login_required
@no_csrf
def index():
    context = {'rest_list_path': router.to_path(rest.index),
               'rest_new_path': router.to_path(rest.new)}
    return TemplateResponse(context, 'courses/course_home.html')


def delete(course_id):
    course_facade.delete_course_cmd(course_id)()
    return RedirectResponse(router.to_path(index))

