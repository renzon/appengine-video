# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from course_app import course_facade


def index():
    cmd = course_facade.list_courses_cmd()
    course_list = cmd()
    course_form = course_facade.course_form()
    course_dcts = [course_form.fill_with_model(m) for m in course_list]
    return JsonResponse(course_dcts)


def new(_resp, **course_properties):
    cmd = course_facade.save_course_cmd(**course_properties)
    return _save_or_update_json_response(cmd, _resp)


def edit(_resp, id, **course_properties):
    cmd = course_facade.update_course_cmd(id, **course_properties)
    return _save_or_update_json_response(cmd, _resp)


def delete(_resp, id):
    cmd = course_facade.delete_course_cmd(id)
    try:
        cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)


def _save_or_update_json_response(cmd, _resp):
    try:
        course = cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)
    course_form = course_facade.course_form()
    return JsonResponse(course_form.fill_with_model(course))

