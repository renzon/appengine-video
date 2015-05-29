# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json

from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandParallel
from gaebusiness.gaeutil import UrlFetchCommand
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.router import to_path


def _chamar_api(repo_cmd, usuario_cmd):
    CommandParallel(usuario_cmd, repo_cmd).execute()
    usuario_json = usuario_cmd.result.content
    repos_json = repo_cmd.result.content
    return repos_json, usuario_json


@login_not_required
@no_csrf
def index(nome):
    url_base = 'https://api.github.com/users'
    url_usuario = to_path(url_base, nome)
    url_repos = to_path(url_usuario, 'repos')
    usuario_cmd = UrlFetchCommand(url_usuario, headers={'Accept': 'application/vnd.github.v3+json'})
    repo_cmd = UrlFetchCommand(url_repos, headers={'Accept': 'application/vnd.github.v3+json'})
    repos_json, usuario_json = _chamar_api(repo_cmd, usuario_cmd)
    usuario_dct = json.loads(usuario_json)
    repos_dct = json.loads(repos_json)
    contexto = {'nome': nome,
                'avatar': usuario_dct['avatar_url'],
                'repos': [(r['name'], r['html_url']) for r in repos_dct]}
    return TemplateResponse(contexto, 'github.html')