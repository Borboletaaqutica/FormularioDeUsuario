import tkinter as tk
from tkinter import messagebox

# Função principal
def processar():
    nome = entry_nome.get()
    idade_str = entry_idade.get()
    pergunta = var_pet.get()

    if not idade_str.isdigit():
        messagebox.showerror("Erro", "Por favor, insira uma idade válida.")
        return

    idade = int(idade_str)
    idade_futura = idade + 15
    resultado = f"{nome}, você terá {idade_futura} anos em 15 anos.\n"

    if pergunta == "s":
        nome_animal = entry_animal.get()
        if nome_animal.strip() == "":
            resultado += "Você disse que tem um animal, mas não disse o nome dele!"
        else:
            resultado += f"{nome_animal.capitalize()} deve ser uma fofura!"
    elif pergunta == "n":
        resultado += "Ok, sem problemas!"
    else:
        resultado += "Resposta inválida."

    label_resultado.config(text=resultado)

# Estilo CassSoft 95
fundo = "#C0C0C0"
fonte_padrao = ("Microsoft Sans Serif", 10)

janela = tk.Tk()
janela.title("CassSoft 95™ - Entrevista Interativa")
janela.geometry("420x400")
janela.configure(bg=fundo)

# Título fake estilo app Win95
tk.Label(janela, text="🖥️ CassSoft 95™ - Formulário de Usuário", bg=fundo, font=("Microsoft Sans Serif", 11, "bold")).pack(pady=5)

# Nome
tk.Label(janela, text="Qual é o seu nome?", bg=fundo, font=fonte_padrao).pack()
entry_nome = tk.Entry(janela, relief="sunken", bd=2, font=fonte_padrao)
entry_nome.pack(pady=2)

# Idade
tk.Label(janela, text="Qual a sua idade?", bg=fundo, font=fonte_padrao).pack()
entry_idade = tk.Entry(janela, relief="sunken", bd=2, font=fonte_padrao)
entry_idade.pack(pady=2)

# Animal de estimação
tk.Label(janela, text="Você tem um animal de estimação?", bg=fundo, font=fonte_padrao).pack()
var_pet = tk.StringVar(value="n")
frame_radio = tk.Frame(janela, bg=fundo)
tk.Radiobutton(frame_radio, text="Sim", variable=var_pet, value="s", bg=fundo, font=fonte_padrao).pack(side="left", padx=5)
tk.Radiobutton(frame_radio, text="Não", variable=var_pet, value="n", bg=fundo, font=fonte_padrao).pack(side="left", padx=5)
frame_radio.pack()

# Nome do animal
tk.Label(janela, text="Se sim, qual o nome do animal?", bg=fundo, font=fonte_padrao).pack()
entry_animal = tk.Entry(janela, relief="sunken", bd=2, font=fonte_padrao)
entry_animal.pack(pady=2)

# Botão enviar
tk.Button(janela, text="Enviar", command=processar, relief="raised", bd=3, font=fonte_padrao).pack(pady=10)

# Resultado
label_resultado = tk.Label(janela, text="", bg=fundo, wraplength=350, justify="left", font=fonte_padrao)
label_resultado.pack(pady=10)

janela.mainloop()
