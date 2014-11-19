# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandParallel
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand, SingleModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from venda_app.venda_model import Venda, NOVA, CONTABILIZADA


class VendaSaveForm(ModelForm):
    """
    Form used to save and update Venda
    """
    _model_class = Venda
    _include = [Venda.preco]


class VendaForm(ModelForm):
    """
    Form used to expose Venda's properties for list or json
    """
    _model_class = Venda


class SaveVendaCommand(SaveCommand):
    _model_form_class = VendaSaveForm


class UpdateVendaCommand(UpdateNode):
    _model_form_class = VendaSaveForm


class ListVendaCommand(ModelSearchCommand):
    def __init__(self):
        super(ListVendaCommand, self).__init__(Venda.query_by_creation())


class BuscarVendaPorStatusCmd(SingleModelSearchCommand):
    def __init__(self, status=NOVA, start_cursor=None, offset=0, use_cache=False):
        super(BuscarVendaPorStatusCmd, self).__init__(Venda.query_by_stats_order_by_creation(status), start_cursor,
                                                      offset, use_cache)


class ContabilizarVendaCmd(CommandParallel):
    def __init__(self, start_cursor=None):
        self.cursor = None
        cmd = BuscarVendaPorStatusCmd(NOVA, start_cursor=start_cursor)
        self._busca_cmd = cmd
        super(ContabilizarVendaCmd, self).__init__(cmd)

    def do_business(self):
        super(ContabilizarVendaCmd, self).do_business()
        self.cursor = self._busca_cmd.cursor
        venda = self.result
        if venda:
            venda.status = CONTABILIZADA
            self._to_commit = venda



