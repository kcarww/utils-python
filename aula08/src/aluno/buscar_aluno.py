from aluno_repositorio import alunos

def buscar_por_matricula(matricula: int):
    for aluno in alunos:
        if aluno['matricula'] == matricula:
            return aluno
    return None

if __name__ == '__main__':
    print(buscar_por_matricula(1))
    print(buscar_por_matricula(-1)) # None