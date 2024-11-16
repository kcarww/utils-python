from aluno_repositorio import alunos

def listar_alunos():
    print('--- ALUNOS MATRICULADOS ---')
    for aluno in alunos:
        print(f"Matricula: {aluno['matricula']}")
        print(f"nome: {aluno['nome']}")
        print(f"curso(s): {aluno['curso']}")
        print(f"Nota: {aluno['nota']}")
        print('-'*50)

if __name__ == "__main__":
    listar_alunos()