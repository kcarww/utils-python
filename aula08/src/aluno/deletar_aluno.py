from aluno_repositorio import alunos
from buscar_aluno import buscar_por_matricula

def deletar_aluno(matricula: int):
    aluno = buscar_por_matricula(matricula)
    if aluno:
        alunos.remove(aluno)
        return
    print('Aluno não encontrado!')

if __name__ == '__main__':
    print(alunos)
    deletar_aluno(1)
    print(alunos)
    deletar_aluno(1)
    