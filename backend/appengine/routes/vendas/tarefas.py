# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import logging
from google.appengine.api import taskqueue
from gaebusiness.gaeutil import TaskQueueCommand
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.router import to_path


@login_not_required
@no_csrf
def contagem(total='0', cursor=None):
    # buscar um pagamento
    # incremetar o total das vendas
    # faço a busca novamente
    total = int(total)
    logging.info('Total = %s' % total)
    total += 1
    if total < 3:
        cmd = TaskQueueCommand('rapida', to_path(contagem), params={'total': str(total)})
        cmd()