# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from decimal import Decimal
import logging
from google.appengine.api import taskqueue
from gaebusiness.gaeutil import TaskQueueCommand
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.router import to_path
from venda_app import venda_facade


@login_not_required
@no_csrf
def contagem(total='0.00', cursor=None):
    busca_cmd = venda_facade.contabilizar_venda_cmd(cursor)
    venda = busca_cmd()
    if venda is None:
        logging.info(total)
    else:
        total = Decimal(total)
        total += venda.preco
        cmd = TaskQueueCommand('rapida', to_path(contagem),
                               params={'total': str(total), 'cursor': busca_cmd.cursor.urlsafe()})
        cmd()