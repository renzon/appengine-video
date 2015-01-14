# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode, NodeSearch, DeleteNode
from course_app.course_model import Course



class CourseSaveForm(ModelForm):
    """
    Form used to save and update Course
    """
    _model_class = Course
    _include = [Course.nome]


class CourseForm(ModelForm):
    """
    Form used to expose Course's properties for list or json
    """
    _model_class = Course


class GetCourseCommand(NodeSearch):
    _model_class = Course


class DeleteCourseCommand(DeleteNode):
    _model_class = Course


class SaveCourseCommand(SaveCommand):
    _model_form_class = CourseSaveForm


class UpdateCourseCommand(UpdateNode):
    _model_form_class = CourseSaveForm


class ListCourseCommand(ModelSearchCommand):
    def __init__(self):
        super(ListCourseCommand, self).__init__(Course.query_by_creation())

