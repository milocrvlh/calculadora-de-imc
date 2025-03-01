from customtkinter import *
from tkinter import messagebox

def cadastrar_produto():

    produto = campo_produto.get()
    preco = campo_preco.get()
    quantidade = campo_quantidade.get()    
    

    if "" in [produto, preco, quantidade]:
        messagebox.showwarning(
            title='Atenção',

            message='Preencha todos os campos antes de cadastrar.'
                            )
    else:
        messagebox.showinfo(
            title='Cadastro realizado',
            message=f'Você cadastrou {quantidade} unidades de {produto}, com o valor unitário de {preco} reais.'
        )
        with open(".\exercicios_base\cadastro.txt", 'a') as arquivo:
            arquivo.write(f'{produto},{preco},{quantidade}\n')


    campo_produto.delete(0,"end")
    campo_preco.delete(0,"end")
    campo_quantidade.delete(0,"end")
    campo_produto.focus()
    

root = CTk()
root.geometry("275x300")
root.minsize(200,300)
root.title("Cadastro de Produtos")

CTkLabel(root, text="Produto").pack(pady=5)
campo_produto = CTkEntry(root, placeholder_text="Produto")
campo_produto.pack()

CTkLabel(root, text="Preço").pack(pady=5)
campo_preco = CTkEntry(root, placeholder_text="Preço")
campo_preco.pack()

CTkLabel(root, text="Quantidade").pack(pady=5)
campo_quantidade = CTkEntry(root, placeholder_text="Quantidade")
campo_quantidade.pack()


CTkButton(root, text="Cadastrar", command=cadastrar_produto).pack(pady=20)
root.mainloop()