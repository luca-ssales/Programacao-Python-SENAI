import tkinter as tk
from tkinter import messagebox

#verifica se o login e senha sao admin 123
def verificar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if usuario == "admin" and senha == "1234":
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
    else:
        messagebox.showerror("Erro", "Usuário ou senha inválidos!")

# Janela principal
janela = tk.Tk() #crie a janela

janela.title("Sistema de Login") #coloquei o nome q aparece em cima

janela.geometry("300x400") #defini o tamanho q sera exibido 

janela.resizable(False, False)
janela.configure(bg="#1e1e2e") #defini a cor do fundo 


# Título
titulo = tk.Label(
    janela, # vai estar ana janela
    text="LOGIN 👤", #titulo login
    font=("Arial", 20, "bold"), #tam e estilo da fonte
    bg="#1e1e2e", #cor do fundo
    fg="white" #cor do texto
)
titulo.pack(pady=20)

# Usuário
label_usuario = tk.Label(
    janela,
    text="Usuário",
    font=("Arial", 10),
    bg="#1e1e2e",
    fg="white"
)
label_usuario.pack()

entry_usuario = tk.Entry(
    janela,
    font=("Arial", 12),
    justify="center"
)
entry_usuario.pack(pady=5)

# Senha
label_senha = tk.Label(
    janela,
    text="Senha",
    font=("Arial", 10),
    bg="#1e1e2e",
    fg="white"
)
label_senha.pack()

entry_senha = tk.Entry(
    janela,
    font=("Arial", 12),
    show="*",
    justify="center"
)
entry_senha.pack(pady=5)

# Botão
btn_login = tk.Button(
    janela,
    text="Entrar",
    font=("Arial", 11, "bold"),
    bg="#4CAF50",
    fg="white",
    width=15,
    cursor="hand2",
    command=verificar_login
)
btn_login.pack(pady=20)

janela.mainloop()