from banco import Livraria, Livro
import flet as ft


def main(page: ft.Page):
    page.title = 'Livraria'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def cadastrar(e):
        titulo = txt_titulo.value
        autor = txt_autor.value
        ano_publicacao = txt_ano_publicacao.value

        livro = Livro(titulo, autor, ano_publicacao)
        livraria.adicionar_livro(livro)
        atualizar_tabela()
        limpar_campos()
        dialog = ft.AlertDialog(
            title=ft.Text('Livro cadastrado com sucesso!')
        )
        page.dialog = dialog
        dialog.open = True
        page.update()

    def editar(e):
        id = int(txt_id.value)
        titulo = txt_titulo.value
        autor = txt_autor.value
        ano_publicacao = int(txt_ano_publicacao.value)
        livro = Livro(titulo, autor, ano_publicacao)
        livro.id = id
        if livraria.editar_livro(livro):
            atualizar_tabela()
            limpar_campos()
            dialog = ft.AlertDialog(
            title=ft.Text('Livro alterado com sucesso!')
        )
        else:
            dialog = ft.AlertDialog(
            title=ft.Text('Livro não encontrado!')
        )
        page.dialog = dialog
        dialog.open = True
        page.update()

    def deletar(e):
        id = int(txt_id.value)
        if livraria.remover_livro(id):
            atualizar_tabela()
            limpar_campos()
            dialog = ft.AlertDialog(
            title=ft.Text('Livro alterado com sucesso!')
        )
        else:
            dialog = ft.AlertDialog(
            title=ft.Text('Livro não encontrado!')
        )
        page.dialog = dialog
        dialog.open = True
        page.update()

    def limpar_campos():
        txt_id.value = ''
        txt_titulo.value = ''
        txt_autor.value = ''
        txt_ano_publicacao.value = ''
        txt_buscar.value = ''
        page.update()

    def selecionar_linha(e, book):
        limpar_campos()
        txt_id.value = str(book.id)
        txt_titulo.value = book.titulo
        txt_autor.value = book.autor
        txt_ano_publicacao.value = book.ano_publicacao
        page.update()

    def atualizar_tabela():
        livros = livraria.listar_livros()
        if txt_buscar.value != '':
            livros = livraria.buscar_livro_por_titulo(txt_buscar.value)
        tabela.rows = []
        for book in livros:
            row = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(book.id)),
                    ft.DataCell(ft.Text(book.titulo)),
                    ft.DataCell(ft.Text(book.autor)),
                    ft.DataCell(ft.Text(book.ano_publicacao)),
                ], on_select_changed=lambda e, b=book: selecionar_linha(e, b)
            )
            tabela.rows.append(row)

        page.update()

    txt_id = ft.TextField(label='ID', disabled=True)
    txt_titulo = ft.TextField(label='Titulo')
    txt_autor = ft.TextField(label='autor')
    txt_ano_publicacao = ft.TextField(label='Ano de Publicação')

    btn_enviar = ft.ElevatedButton(text="Enviar", on_click=cadastrar)
    btn_editar = ft.ElevatedButton(text="Editar", on_click=editar)
    btn_excluir = ft.ElevatedButton(text="Excluir", on_click=deletar)

    btn_rows = ft.Row(controls=[
        btn_enviar,
        btn_editar,
        btn_excluir
    ])

    tabela = ft.DataTable(columns=[
        ft.DataColumn(ft.Text('ID')),
        ft.DataColumn(ft.Text('Titulo')),
        ft.DataColumn(ft.Text('Autor')),
        ft.DataColumn(ft.Text('Ano de Publicação'), numeric=True),

    ])

    txt_buscar = ft.TextField(label='Buscar livro (titulo)', on_change=lambda e: atualizar_tabela())

    page.add(txt_id, txt_titulo,
             txt_autor,
             txt_ano_publicacao,
             btn_rows,
             tabela,
             txt_buscar)
    page.update()


livraria = Livraria('Livraria Flet', 'Rua Flet, 123')

ft.app(main)
