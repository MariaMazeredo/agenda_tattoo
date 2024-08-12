import tkinter as tk
from tkinter import messagebox, simpledialog

def main():
    # Criando a janela principal
    root = tk.Tk()
    root.title("Agenda Tattoo")
    root.geometry("400x400")

    clientes = []

    # Funções para os botões
    def adicionar_cliente():
        nome = entry_nome.get()
        telefone = entry_telefone.get()
        email = entry_email.get()
        data = entry_data.get()
        valor = entry_valor.get()
        cliente = {
            'nome': nome,
            'telefone': telefone,
            'email': email,
            'data': data,
            'valor': valor
        }
        clientes.append(cliente)
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        limpar_campos()

    def listar_clientes():
        if not clientes:
            messagebox.showinfo("Informação", "Não há clientes agendados")
        else:
            lista = ""
            for i, cliente in enumerate(clientes):
                lista += (f"Cliente {i + 1}\n"
                          f"Nome: {cliente['nome']}\n"
                          f"Telefone: {cliente['telefone']}\n"
                          f"Email: {cliente['email']}\n"
                          f"Data: {cliente['data']}\n"
                          f"Valor: {cliente['valor']}\n\n")
            messagebox.showinfo("Clientes", lista)

    def deletar_cliente():
        if not clientes:
            messagebox.showinfo("Informação", "Não há clientes para deletar.")
            return

        indice = entry_id.get()
        if indice.isdigit():
            indice = int(indice) - 1
            if 0 <= indice < len(clientes):
                cliente_removido = clientes.pop(indice)
                messagebox.showinfo("Sucesso", f"Cliente {cliente_removido['nome']} deletado com sucesso!")
            else:
                messagebox.showerror("Erro", "Índice inválido. Tente novamente.")
        else:
            messagebox.showerror("Erro", "Entrada inválida. Por favor, insira um número.")

    def limpar_campos():
        entry_nome.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_data.delete(0, tk.END)
        entry_valor.delete(0, tk.END)
        entry_id.delete(0, tk.END)

    # Widgets para entrada de dados
    tk.Label(root, text="Nome").pack()
    entry_nome = tk.Entry(root)
    entry_nome.pack()

    tk.Label(root, text="Telefone").pack()
    entry_telefone = tk.Entry(root)
    entry_telefone.pack()

    tk.Label(root, text="Email").pack()
    entry_email = tk.Entry(root)
    entry_email.pack()

    tk.Label(root, text="Data (DD/MM/AAAA)").pack()
    entry_data = tk.Entry(root)
    entry_data.pack()

    tk.Label(root, text="Valor").pack()
    entry_valor = tk.Entry(root)
    entry_valor.pack()

    # Botões
    tk.Button(root, text="Cadastrar Cliente", command=adicionar_cliente).pack(pady=5)
    tk.Button(root, text="Listar Clientes", command=listar_clientes).pack(pady=5)
    
    tk.Label(root, text="ID para deletar").pack()
    entry_id = tk.Entry(root)
    entry_id.pack()
    tk.Button(root, text="Deletar Cliente", command=deletar_cliente).pack(pady=5)

    tk.Button(root, text="Sair", command=root.quit).pack(pady=20)

    # Iniciar a interface
    root.mainloop()

main()
