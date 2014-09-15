# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from livro_app.comandos import ListarLivrosDeAutor


def listar_livros_de_autor_cmd(autor):
    """
    Função que cria um comando que retorna lista de livros de um autor ordenados por sua data de criação
    :param autor: O autor do livro, em geral, uma instancia ou id de usuário
    :return: Instância de Command
    """

    return ListarLivrosDeAutor(autor)

