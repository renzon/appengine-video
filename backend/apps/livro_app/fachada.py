# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandParallel
from gaegraph.business_base import NodeSearch, DeleteNode
from gaegraph.model import to_node_key
from livro_app.comandos import ListarLivrosDeAutor, BookFormTable, BookForm, EditarLivro, ApagarAutorArcos, \
    SalvarLivroComAutor


def listar_livros_de_autor_cmd(autor):
    """
    Função que cria um comando que retorna lista de livros de um autor ordenados por sua data de criação
    :param autor: O autor do livro, em geral, uma instancia ou id de usuário, ou um comando que retorne o autor como
    resultado de sua execução
    :return: Instância de Command
    """

    return ListarLivrosDeAutor(autor)


def livro_tabela_form(**propriedades):
    return BookFormTable(**propriedades)


def livro_form(**propriedades):
    return BookForm(**propriedades)


def get_livro(livro_id):
    return NodeSearch(livro_id)


def editar_livro(livro_id, **propriedades):
    return EditarLivro(to_node_key(livro_id), **propriedades)


def apagar_livro_cmd(livro_id):
    apagar_cmd = DeleteNode(livro_id)
    apagar_arcos = ApagarAutorArcos(livro_id)
    return CommandParallel(apagar_cmd, apagar_arcos)


def salvar_livro(autor, **propriedades):
    return SalvarLivroComAutor(autor, **propriedades)