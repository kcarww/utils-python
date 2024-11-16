from aluno_repositorio import alunos
from buscar_aluno import buscar_por_matricula

def editar_aluno(
    matricula: int,
        nome: str,
        curso: set,
        nota: float
):
    aluno =buscar_por_matricula(matricula)
    if aluno:
        aluno['nome'] = nome
        aluno['curso'] = curso
        aluno['nota'] = nota
        return
    print('Aluno não encontrado!')


if __name__ == '__main__':
    editar_aluno(1, 'Luquinha do grau', {1,2,3,4}, 8.5)
    print(alunos)
