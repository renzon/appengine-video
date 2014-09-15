# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandParallel, CommandExecutionException
from gaecookie.decorator import no_csrf
from gaegraph.business_base import DeleteNode, NodeSearch
from gaegraph.model import to_node_key
from livro_app import fachada
from livro_app.comandos import BookFormTable, BookForm, EditarLivro, ApagarAutorArcos, \
    SalvarLivroComAutor
from tekton import router
from tekton.gae.middleware.redirect import RedirectResponse

# Handlers

@no_csrf
def index(_logged_user):
    buscar_livros_cmd = fachada.listar_livros_de_autor_cmd(_logged_user)
    livro_lista = buscar_livros_cmd()
    book_form = BookFormTable()
    livro_lista = [book_form.fill_with_model(livro) for livro in livro_lista]
    editar_form_path = router.to_path(editar_form)
    delete_path = router.to_path(delete)
    for livro in livro_lista:
        livro['edit_path'] = '%s/%s' % (editar_form_path, livro['id'])
        livro['delete_path'] = '%s/%s' % (delete_path, livro['id'])
    contexto = {'livro_lista': livro_lista,
                'form_path': router.to_path(form)}
    return TemplateResponse(contexto)


@no_csrf
def editar_form(book_id):
    busca_cmd = NodeSearch(book_id)
    book = busca_cmd()
    book_form = BookForm()
    book_form.fill_with_model(book)
    contexto = {'salvar_path': router.to_path(editar, book_id),
                'book': book_form}
    return TemplateResponse(contexto, 'books/form.html')


def editar(book_id, **propriedades):
    editar_cmd = EditarLivro(to_node_key(book_id), **propriedades)
    try:
        editar_cmd()
        return RedirectResponse(router.to_path(index))

    except CommandExecutionException:
        contexto = {'salvar_path': router.to_path(salvar),
                    'erros': editar_cmd.errors,
                    'book': propriedades}
        return TemplateResponse(contexto, 'books/form.html')


@no_csrf
def form():
    contexto = {'salvar_path': router.to_path(salvar)}
    return TemplateResponse(contexto)


def delete(book_id):
    apagar_cmd = DeleteNode(book_id)
    apagar_arcos = ApagarAutorArcos(book_id)
    comandos_paralelos = CommandParallel(apagar_cmd, apagar_arcos)
    comandos_paralelos()
    return RedirectResponse(router.to_path(index))


def salvar(_logged_user, **propriedades):
    salvar_livro_com_autor_cmd = SalvarLivroComAutor(_logged_user, **propriedades)
    try:
        salvar_livro_com_autor_cmd()
        return RedirectResponse(router.to_path(index))
    except CommandExecutionException:
        contexto = {'salvar_path': router.to_path(salvar),
                    'erros': salvar_livro_com_autor_cmd.errors,
                    'book': propriedades}
        return TemplateResponse(contexto, 'books/form.html')








