from aluno_repositorio import alunos
from validator import validate

matricula_atual = 1

def adicionar_aluno(nome: str, curso: set, nota: float):
    global matricula_atual
    validate(nome, curso, nota)
    matricula_atual += 1
    aluno = {
        "matricula": matricula_atual,
        "nome": nome,
        "curso": curso,
        "nota": nota,
    }
    alunos.append(aluno)


if __name__ == "__main__":
    adicionar_aluno(
        nome="Cleitin python",
        curso={1},
        nota=10
        )
    print(alunos)