from customtkinter import *

set_appearance_mode('dark')

root = CTk()
root.geometry("300x300")
root.minsize(250, 275)
root.title("Tela de Cadastro")

def cadastrar():
    nome = campo_nome.get()
    idade = campo_idade.get()
    print(f"Você cadastrou {nome} com a idade {idade}.")

CTkLabel(root, text="CADASTRO DE USUÁRIO").pack(pady=15)

CTkLabel(root, text="Nome:").pack()

campo_nome = CTkEntry(root, placeholder_text="Digite o nome")
campo_nome.pack(pady=5)

CTkLabel(root, text="Idade:").pack()

campo_idade = CTkEntry(root, placeholder_text="Digite o idade")
campo_idade.pack(pady=5)

CTkButton(root, text="Cadastrar", command=cadastrar).pack(pady=15)


root.mainloop()