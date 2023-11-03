try:
    menu = int(input("Selecione: \n 1. Decimal para binário \n 2. Binário para decimal\n Opção: "))
    if menu < 1 or menu > 2:
        raise ValueError
    if menu == 1:
        dec = int(input("Informe o seu valor decimal: : "))
        print(f"Binario: {bin(dec)[2:]}")
    elif menu == 2:
        binary = input("Informe o seu valor binário ")
        print(f"Decimal: {int(binary, 2)}")
except ValueError:
    print ("Opção inválida")
