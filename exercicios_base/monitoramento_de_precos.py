from customtkinter import *

root = CTk()
root.geometry("350x460")
root.title("Monitoramento de Preços")
root.minsize(350, 460)
root.configure(padx=40, pady=20)


def modificarlabelslider(valor):
    texto_variavel.configure(text=f"Tempo de execução em minutos: {int(valor)}")

def iniciar_varredura():
    decisao_baixar_relatorio = baixar_relatorio.get()
    decisao_notificar_email = notificar_email.get()
    decisao_visualizacao = controle_radiobutton.get()
    tempo_execucao = int(slider.get())

    print("O navegador iniciará de forma visível.") if decisao_visualizacao else print("O navegador iniciará de forma invisível.")

    print("O relatório de preços será baixado.") if decisao_baixar_relatorio else print("O relatório de preços não será baixado.")

    print("Ao final da execução, você será notificado por e-mail") if decisao_notificar_email else print("Ao final da execução, você não será notificado por e-mail")

    print(f"A automação será executada por {tempo_execucao}") 

CTkLabel(root, text="Marque as funcionalidades que deseja incluir:").grid(row=0, column=0, pady=10)

baixar_relatorio = CTkCheckBox(root, text="Baixar relatório de preços")
baixar_relatorio.grid(row=1,column=0, pady=10, sticky='w')

notificar_email =CTkCheckBox(root, text="Notificar finalização por e-mail")
notificar_email.grid(row=2,column=0, pady=10, sticky='w')

CTkLabel(root, text="Visualizar o navegador durante a automação?").grid(row=3, column=0, pady=10, sticky='w')


controle_radiobutton = BooleanVar()


CTkRadioButton(root, text="Sim", value=True, variable=controle_radiobutton).grid(row=4,column=0, pady=10, sticky='w')   
CTkRadioButton(root, text="Não", value=False, variable=controle_radiobutton).grid(row=5,column=0, pady=10, sticky='w')

slider = CTkSlider(root, from_=1, to=60, command=modificarlabelslider)
slider.grid(row=7, column=0, pady=10, sticky='w')
slider.set(1)


valor_inicial_slider = int(slider.get())

texto_variavel = CTkLabel(root, text=f"Tempo de execução em minutos: {valor_inicial_slider}")
texto_variavel.grid(row=6, column=0, pady=10, sticky='w')

CTkButton(root, text="Iniciar automação", command=iniciar_varredura).grid(row=8, column=0, pady=10, sticky='w')


root.mainloop()


