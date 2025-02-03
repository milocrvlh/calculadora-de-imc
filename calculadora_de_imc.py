from customtkinter import *

set_appearance_mode('dark')

def classificar_imc(imc: float) -> None:
    if imc < 17:
        print("Muito abaixo do peso")
    elif 17 <= imc and imc < 18.5:
        print("Abaixo do peso")
    elif 18.5 <= imc and imc < 25:
        print("Peso normal")
    elif 25 <= imc and imc < 30:
        print("Acima do peso")
    elif 30 <= imc and imc < 35:
        print("Obesidade I")
    elif 35 <= imc and imc < 40:
        print("Obesidade II (severa)")
    else:
        print("Obesidade III (mórbida)")

def calcular_imc():
    peso = float(campo_peso.get())
    altura = float(campo_altura.get())
    imc = peso / altura ** 2
    print(f"o IMC é {imc}.")
    classificar_imc(imc)



root = CTk()
root.geometry("275x220")
root.minsize(200,200)
root.title("Calculadora de IMC")

CTkLabel(root, text="Peso (em Kg)").pack(pady=(10, 0))

campo_peso = CTkEntry(root, placeholder_text="Insira seu peso")
campo_peso.pack(pady=5)


CTkLabel(root, text="Altura (em m)").pack()
campo_altura = CTkEntry(root, placeholder_text="Insira sua altura")
campo_altura.pack(pady=5)

CTkButton(root, text="Calcular", command=calcular_imc).pack(pady=15)


root.mainloop()
