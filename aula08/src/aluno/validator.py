def validate(nome: str, curso: set, nota: float):
    # Valida se o nome é maior que 255 caracteres
    if len(nome) > 255:
        raise ValueError("Nome muito longo!!")
    
    # Valida se o curso é um set
    if not isinstance(curso, set):
        raise TypeError("Curso deve ser um SET")
    
    if nota < 0 or nota > 10:
        raise ValueError("Nota fora do intervalo aceito!")

