class Livro:
    id = 0
    def __init__(self, titulo: str, autor: str, ano_publicacao: int):
        Livro.id += 1
        self.id = Livro.id
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao


class Livraria:
    def __init__(self, nome: str, endereco: str):
        self.nome = nome
        self.endereco = endereco
        self.livros = []
        
    def adicionar_livro(self, livro: Livro):
        self.livros.append(livro)
        
    def listar_livros(self):
        return self.livros
    
    def buscar_livro_por_titulo(self, titulo: str):
        for livro in self.livros:
            if livro.titulo == titulo:
                return livro
        return None
    
    def remover_livro(self, id: int):
        for livro in self.livros:
            if livro.id == id:
                self.livros.remove(livro)
                return True
        return False
    
    def editar_livro(self, book: Livro):
        for livro in self.livros:
            if livro.id == book.id:
                livro.titulo = book.titulo
                livro.autor = book.autor
                livro.ano_publicacao = book.ano_publicacao
                return True
        return False
    
    
