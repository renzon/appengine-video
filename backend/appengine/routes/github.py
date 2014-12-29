# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from google.appengine.api import urlfetch
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandParallel
from gaebusiness.gaeutil import UrlFetchCommand
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.router import to_path


@login_not_required
@no_csrf
def index(_resp, nome):
    url_base = 'https://api.github.com/users'
    url_usuario = to_path(url_base, nome)
    url_repos = to_path(url_usuario, 'repos')
    usuario_cmd = UrlFetchCommand(url_usuario, headers={'Accept': 'application/vnd.github.v3+json'})
    repo_cmd = UrlFetchCommand(url_repos, headers={'Accept': 'application/vnd.github.v3+json'})
    CommandParallel(usuario_cmd, repo_cmd).execute()
    usuario_json = json.loads(usuario_cmd.result.content)
    repo_json = json.loads(repo_cmd.result.content)
    contexto = {'nome': nome,
                'avatar': usuario_json['avatar_url'],
                'repos': [(r['name'], r['html_url']) for r in repo_json]}
    return TemplateResponse(contexto, 'github.html')