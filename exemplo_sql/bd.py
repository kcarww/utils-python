# pymysql
import pymysql.cursors
try:
    # connection => abre a conexão com o banco de dados
    conexao = pymysql.connect(host='localhost',
                              user='root',
                              password='',
                              database='escola',
                              cursorclass=pymysql.cursors.DictCursor)
    print('Conexão estabelecida com sucesso!')
except Exception as erro:
    print(f'Erro ao conectar com o banco: {erro}')


# cursor
cursor = conexao.cursor()

def select():
    try:
        sql = "SELECT * FROM alunos"
        cursor.execute(sql)
        # fetch() => Separando os alunos da tabela
        alunos = cursor.fetchall()
        for aluno in alunos:
            print(f'Nome: {aluno["nome"]} - Nota: {aluno["nota"]}')
    except Exception as error:
        print(f'Erro ao buscar: {error}')

# select()


def insert(nome, idade, nota):
    try:
        sql = "INSERT INTO alunos (nome, idade, nota)" \
              "VALUES (%s, %s, %s)"
        cursor.execute(sql, (nome, idade, nota))
        conexao.commit()
        print('Dados cadastrados com sucesso!')
    except Exception as error:
        print(f'Erro ao cadastrar: {error}')

# insert("Luan Lopes", 23, 9.5)
# select()

def update(nome, idade, nota, matricula):
    try:
        sql = "UPDATE alunos SET nome = %s, idade = %s," \
              "nota = %s WHERE matricula = %s"
        cursor.execute(sql, (nome, idade, nota, matricula))
        conexao.commit()
        print('Dados alterados com sucesso!')
    except Exception as error:
        print(f'Erro ao atualizar os dados: {error}')

# update('Leticia Mota', 25, 9.7, 1)
# select()

def delete(matricula):
    try:
        if alunoExiste(matricula):
            sql = "DELETE FROM alunos WHERE matricula = %s"
            cursor.execute(sql, matricula)
            conexao.commit()
            print('Aluno deletado com sucesso!')
        else:
            print('Aluno não encontrado!')
    except Exception as error:
        print(f'Erro ao deletar aluno: {error}')


def alunoExiste(matricula):
    try:
        sql = "SELECT * FROM alunos WHERE matricula = %s"
        cursor.execute(sql, matricula)
        if len(cursor.fetchall()) == 1:
            return True
        else:
            return False
    except Exception as error:
        print(f'Erro ao consultar dados: {error}')

# delete(1)  # error
# delete(2)  # success
# select()
