# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from datetime import date
from base import GAETestCase
from gaebusiness.business import CommandExecutionException
from gaepermission.model import MainUser
from livro_app import fachada
from mommygae import mommy


class SalvarLivroTests(GAETestCase):
    def test_com_erros_de_validacao(self):
        usuario = mommy.save_one(MainUser)
        salvar_cmd = fachada.salvar_livro(usuario, title='', price='asdad', release='02asdfasdf')
        self.assertRaises(CommandExecutionException, salvar_cmd)
        erros = salvar_cmd.errors
        self.assertIn('title', erros)
        self.assertIn('price', erros)
        self.assertIn('release', erros)


    def test_sucesso(self):
        usuario = mommy.save_one(MainUser)
        salvar_cmd = fachada.salvar_livro(usuario, title='App Engine', price='3.44', release='02/03/2015')
        salvar_cmd()

        listar_livros_cmd = fachada.listar_livros_de_autor_cmd(usuario)
        livros = listar_livros_cmd()
        self.assertEqual(1, len(livros))
        livro = livros[0]
        self.assertEqual('App Engine', livro.title)
        self.assertEqual(3.44, livro.price)
        self.assertEqual(date(2015, 2, 3), livro.release)
