# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import logging
from google.appengine.api import taskqueue
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.router import to_path


@login_not_required
@no_csrf
def contagem(total='0'):
    # buscar um pagamento
    # incremetar o total das vendas
    # faço a busca novamente
    total = int(total)
    logging.info('Total = %s' % total)
    total += 1
    if total < 3:
        taskqueue.add(url=to_path(contagem), params={'total': str(total)})