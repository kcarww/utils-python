from tkinter import *
from tkinter import messagebox

def calcular():
    valor_digitado = int(txt_valor.get())
    resto = 0
    resultado = ""
    while valor_digitado > 0:
        resto = valor_digitado % 2
        resultado = str(resto) + resultado
        valor_digitado //= 2
    res.set(f"Resultado é: {resultado}")

janela = Tk()
janela.geometry("300x300")
janela.title("Calculadora binária")
label_valor = Label(janela, text="Valor: ",
                    font="Tahoma 14 bold", fg="blue")
label_valor.grid(row=0, column=0)

txt_valor = Entry(janela, font="Tahoma 14")
txt_valor.grid(row=0, column=1)

button_calcular = Button(janela, font="Tahoma 14", bg="black",
                         fg="yellow", text="Calcular",
                         command=calcular)
button_calcular.grid(row=1, column=0)

res = StringVar()
label_resultado = Label(janela, textvariable=res,
                        font="Tahoma 14 bold", fg="red")
label_resultado.grid(row=2, column=0, columnspan=2)

janela.mainloop()