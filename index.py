from tkinter import *
from tkinter import ttk, messagebox  # Certifique-se de importar o messagebox
import back_end

# Constantes
FONT = ("Arial", 20)
BG_COLOR = "gray"
ENTRY_WIDTH = 53
BUTTON_WIDTH = 30
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600

# Janela
jan = Tk()
jan.title("System Marco")
jan.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.iconbitmap(default="icon/image1.ico")

# Funções auxiliares para criar os widgets
def create_label(frame, text, x, y, font=FONT, width=20, bg="white"):
    label = Label(frame, text=text, font=font, bg=bg, width=width)
    label.place(x=x, y=y)
    return label

def create_entry(frame, x, y, width=ENTRY_WIDTH, show=None):
    entry = ttk.Entry(frame, width=width, show=show)
    entry.place(x=x, y=y)
    return entry

def create_button(frame, text, x, y, command, width=BUTTON_WIDTH):
    button = ttk.Button(frame, text=text, width=width, command=command)
    button.place(x=x, y=y)
    return button

# Alternar entre frames
def show_frame(frame):
    frame.tkraise()

# Função para a tela de registro
def register_screen():
    # Ocultar botões de login e cadastro
    login_button.place_forget()
    register_button.place_forget()

    # Ocultar os campos de login e senha
    user_label.place_forget()
    user_entry.place_forget()
    pass_label.place_forget()
    pass_entry.place_forget()

    # Acrescentar campos de registro
    nome_label = create_label(right_frame, "Nome:", 100, 50)
    nome_entry = create_entry(right_frame, 100, 100)

    email_label = create_label(right_frame, "E-mail:", 100, 150)
    email_entry = create_entry(right_frame, 100, 200)

    login_label = create_label(right_frame, "Login:", 100, 250)
    login_entry = create_entry(right_frame, 100, 300)

    senha_label = create_label(right_frame, "Senha:", 100, 350)
    senha_entry = create_entry(right_frame, 100, 400, show="♣♣♣")

    # Função para integrar db com o botão
    def RegisterUser():
        Name = nome_entry.get()
        Email = email_entry.get()
        User = login_entry.get()
        password = senha_entry.get()

        # Verifica se os campos estão preenchidos
        if not Name or not Email or not User or not password:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return

        try:
            # Inserir no banco de dados
            back_end.cursor.execute("""
            INSERT INTO Users (Name, Email, User, Password) VALUES (?, ?, ?, ?)
            """, (Name, Email, User, password))
            back_end.conn.commit()
            messagebox.showinfo(title="Informação de Registro", message="Conta criada com sucesso.")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao registrar usuário: {e}")
        finally:
            back_end.conn.close()

    # Botões de registro e voltar
    create_button(right_frame, "Registrar", 170, 450, command=RegisterUser)
    create_button(right_frame, "Voltar", 170, 490, command=login_screen)

# Função para a tela de login
def login_screen():
    # Ocultar todos os widgets da tela de registro
    for widget in right_frame.winfo_children():
        widget.place_forget()

    # Acrescentar os campos de login e senha
    global user_label, user_entry, pass_label, pass_entry
    user_label = create_label(right_frame, "User:", 100, 50)
    user_entry = create_entry(right_frame, 100, 100)

    pass_label = create_label(right_frame, "Senha:", 100, 150)
    pass_entry = create_entry(right_frame, 100, 200, show="♥♥♥♥")

    # Botões de login e cadastro
    global login_button, register_button
    login_button = create_button(right_frame, "Login", 160, 300, command=lambda: print("Login feito"))
    register_button = create_button(right_frame, "Cadastro", 160, 350, command=register_screen)

# Criar os frames principais
left_frame = Frame(jan, width=385, height=WINDOW_HEIGHT, bg="black", relief="raised")
left_frame.pack(side=LEFT)

right_frame = Frame(jan, width=570, height=WINDOW_HEIGHT, bg=BG_COLOR, relief="raised")
right_frame.pack(side=RIGHT)

# Inserir imagem no left_frame
logo = PhotoImage(file="icon/logo.png")
logo_label = Label(left_frame, image=logo, bg="black")
logo_label.place(x=10, y=80)

# Iniciar a tela de login
login_screen()

jan.mainloop()
