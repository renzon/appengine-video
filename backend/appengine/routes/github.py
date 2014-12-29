# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.api import urlfetch
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
    usuario_cmd=UrlFetchCommand(url_usuario, headers={'Accept': 'application/vnd.github.v3+json'})
    repo_cmd = UrlFetchCommand(url_repos, headers={'Accept': 'application/vnd.github.v3+json'})
    CommandParallel(usuario_cmd,repo_cmd).execute()
    resultado_usuario = usuario_cmd.result
    resultado = repo_cmd.result
    _resp.write(resultado.content)
    _resp.headerlist.append((str('Content-Type'), str('application/json')))