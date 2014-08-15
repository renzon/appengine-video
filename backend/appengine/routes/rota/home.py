# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required


@login_not_required
@no_csrf
def index(nome):
    class Pessoa(object):
        def __init__(self, nome, sobrenome):
            self.sobrenome = sobrenome
            self.nome = nome

    pessoas = [Pessoa('Renzo', 'Nuccitelli'), Pessoa('Giovane', 'Liberato'),
               Pessoa('Reginaldo','Silva')]

    contexto = {'nome': nome,'pessoas':pessoas}
    return TemplateResponse(contexto)