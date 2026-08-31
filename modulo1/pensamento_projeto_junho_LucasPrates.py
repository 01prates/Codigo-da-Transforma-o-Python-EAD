import tkinter as tk
from tkinter import messagebox, ttk

# --- VARIÁVEIS GLOBAIS ---
p1_nome = "Hambúrguer Clássico"
p1_preco = 22.90
p1_estoque = 100
p1_validade = "10.12.2026"
p1_descricao = "Blend de 150g, queijo, alface e tomate."

p2_nome = ""
p2_preco = 0.0
p2_estoque = 0
p2_validade = ""
p2_descricao = ""

p3_nome = ""
p3_preco = 0.0
p3_estoque = 0
p3_validade = ""
p3_descricao = ""

# --- FUNÇÕES DE LÓGICA E INTERAÇÃO ---

def atualizar_lista_visual():
    """Atualiza o texto da área de estoque com os dados atuais das variáveis."""
    txt_lista.config(state="normal")  # Habilita para edição temporária
    txt_lista.delete('1.0', tk.END)
    global p1_nome, p2_nome, p3_nome
    
    if p1_nome == "" and p2_nome == "" and p3_nome == "":
        txt_lista.insert(tk.END, "Nenhum produto cadastrado no sistema ainda.")
        txt_lista.config(state="disabled")
        return
        
    if p1_nome != "":
        txt_lista.insert(tk.END, f"📌 VAGA 1\nNome: {p1_nome}\nPreço: R$ {p1_preco:.2f}  |  Estoque: {p1_estoque} unid.  |  Validade: {p1_validade}\n")
        txt_lista.insert(tk.END, f"Descrição: {p1_descricao}\n")
        txt_lista.insert(tk.END, "-" * 55 + "\n")
        
    if p2_nome != "":
        txt_lista.insert(tk.END, f"📌 VAGA 2\nNome: {p2_nome}\nPreço: R$ {p2_preco:.2f}  |  Estoque: {p2_estoque} unid.  |  Validade: {p2_validade}\n")
        txt_lista.insert(tk.END, f"Descrição: {p2_descricao}\n")
        txt_lista.insert(tk.END, "-" * 55 + "\n")
        
    if p3_nome != "":
        txt_lista.insert(tk.END, f"📌 VAGA 3\nNome: {p3_nome}\nPreço: R$ {p3_preco:.2f}  |  Estoque: {p3_estoque} unid.  |  Validade: {p3_validade}\n")
        txt_lista.insert(tk.END, f"Descrição: {p3_descricao}\n")
        txt_lista.insert(tk.END, "-" * 55 + "\n")
        
    txt_lista.config(state="disabled")  # Desabilita para o usuário não apagar sem querer

def cadastrar_produto_visual():
    global p1_nome, p1_preco, p1_estoque, p1_validade, p1_descricao
    global p2_nome, p2_preco, p2_estoque, p2_validade, p2_descricao
    global p3_nome, p3_preco, p3_estoque, p3_validade, p3_descricao
    
    nome = ent_nome.get().strip()
    validade = ent_validade.get().strip()
    descricao = ent_desc.get().strip()
    
    if nome == "":
        messagebox.showwarning("Aviso", "O nome do produto não pode ficar em branco.")
        return

    try:
        preco = float(ent_preco.get())
        if preco <= 0:
            messagebox.showerror("Erro", "O preço deve ser maior que zero!")
            return
    except ValueError:
        messagebox.showerror("Erro", "Preço inválido! Digite apenas números (Ex: 25.90).")
        return

    try:
        estoque = int(ent_estoque.get())
        if estoque < 0:
            messagebox.showerror("Erro", "A quantidade de estoque não pode ser negativa!")
            return
    except ValueError:
        messagebox.showerror("Erro", "Estoque inválido! Digite um número inteiro.")
        return

    data_valida = False
    if validade.count('.') == 2:
        partes = validade.split('.')
        if partes[0].isdigit() and partes[1].isdigit() and partes[2].isdigit():
            dia = int(partes[0])
            mes = int(partes[1])
            ano = int(partes[2])
            if 1 <= dia <= 31 and 1 <= mes <= 12 and ano >= 1:
                data_valida = True

    if not data_valida:
        messagebox.showerror("Erro", "Data inválida! Use o formato DD.MM.AAAA\n(Limites: Dia 31, Mês 12).")
        return

    if p1_nome == "":
        p1_nome, p1_preco, p1_estoque, p1_validade, p1_descricao = nome, preco, estoque, validade, descricao
        messagebox.showinfo("Sucesso", f"Produto {p1_nome} cadastrado na vaga 1!")
    elif p2_nome == "":
        p2_nome, p2_preco, p2_estoque, p2_validade, p2_descricao = nome, preco, estoque, validade, descricao
        messagebox.showinfo("Sucesso", f"Produto {p2_nome} cadastrado na vaga 2!")
    elif p3_nome == "":
        p3_nome, p3_preco, p3_estoque, p3_validade, p3_descricao = nome, preco, estoque, validade, descricao
        messagebox.showinfo("Sucesso", f"Produto {p3_nome} cadastrado na vaga 3!")
    else:
        messagebox.showerror("Erro", "❌ Sistema cheio! Limite de 3 produtos atingido.")
        return

    ent_nome.delete(0, tk.END)
    ent_preco.delete(0, tk.END)
    ent_estoque.delete(0, tk.END)
    ent_validade.delete(0, tk.END)
    ent_desc.delete(0, tk.END)
    atualizar_lista_visual()

def realizar_venda_visual():
    global p1_nome, p1_estoque, p1_preco
    global p2_nome, p2_estoque, p2_preco
    global p3_nome, p3_estoque, p3_preco
    
    nome_venda = ent_venda_nome.get().strip()
    
    if p1_nome == "" and p2_nome == "" and p3_nome == "":
        messagebox.showwarning("Erro", "Não há produtos cadastrados para realizar vendas.")
        return

    try:
        qtd_venda = int(ent_venda_qtd.get())
        if qtd_venda <= 0:
            messagebox.showerror("Erro", "A quantidade deve ser maior que zero.")
            return
    except ValueError:
        messagebox.showerror("Erro", "Digite uma quantidade válida (número inteiro).")
        return

    if nome_venda.lower() == p1_nome.lower() and p1_nome != "":
        if qtd_venda <= p1_estoque:
            p1_estoque -= qtd_venda
            total = qtd_venda * p1_preco
            messagebox.showinfo("Venda Concluída", f"✅ Venda realizada! Total: R$ {total:.2f}\nEstoque atual de {p1_nome}: {p1_estoque}")
        else:
            messagebox.showerror("Erro", f"❌ Estoque insuficiente! Temos apenas {p1_estoque}.")
            
    elif nome_venda.lower() == p2_nome.lower() and p2_nome != "":
        if qtd_venda <= p2_estoque:
            p2_estoque -= qtd_venda
            total = qtd_venda * p2_preco
            messagebox.showinfo("Venda Concluída", f"✅ Venda realizada! Total: R$ {total:.2f}\nEstoque atual de {p2_nome}: {p2_estoque}")
        else:
            messagebox.showerror("Erro", f"❌ Estoque insuficiente! Temos apenas {p2_estoque}.")
            
    elif nome_venda.lower() == p3_nome.lower() and p3_nome != "":
        if qtd_venda <= p3_estoque:
            p3_estoque -= qtd_venda
            total = qtd_venda * p3_preco
            messagebox.showinfo("Venda Concluída", f"✅ Venda realizada! Total: R$ {total:.2f}\nEstoque atual de {p3_nome}: {p3_estoque}")
        else:
            messagebox.showerror("Erro", f"❌ Estoque insuficiente! Temos apenas {p3_estoque}.")
    else:
        messagebox.showerror("Erro", "🍔 Erro: Produto não encontrado!")

    ent_venda_nome.delete(0, tk.END)
    ent_venda_qtd.delete(0, tk.END)
    atualizar_lista_visual()

# --- CONFIGURAÇÃO DA JANELA PRINCIPAL ---
janela = tk.Tk()
janela.title("Hamburgueria Sampaio - Sistema de Vendas")
janela.geometry("550x700")
janela.configure(bg="#D32F2F")  # Cor vermelha na parte de fora

# Criando um Canvas e uma Scrollbar para permitir rolagem da tela única
canvas = tk.Canvas(janela, bg="#D32F2F", highlightthickness=0)
scrollbar = ttk.Scrollbar(janela, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#D32F2F")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True, padx=10, pady=10)
scrollbar.pack(side="right", fill="y")

# --- ESTILO DOS COMPONENTES ---
COR_FUNDO = "#D32F2F"  # Vermelho
COR_LETREIRO = "#FFFFFF"  # Branco
COR_BOTAO_BG = "#FFFFFF"  # Branco
COR_BOTAO_FG = "#D32F2F"  # Texto do botão em vermelho para contraste

# --- TÍTULO PRINCIPAL ---
lbl_boas_vindas = tk.Label(scrollable_frame, text="HAMBURGUERIA SAMPAIO", font=("Arial", 18, "bold"), bg=COR_FUNDO, fg=COR_LETREIRO)
lbl_boas_vindas.pack(pady=15)

# --- SEÇÃO 1: CADASTRO DE PRODUTOS ---
frame_cadastro = tk.LabelFrame(scrollable_frame, text=" Cadastrar Novo Hambúrguer ", font=("Arial", 11, "bold"), bg=COR_FUNDO, fg=COR_LETREIRO, padx=10, pady=10)
frame_cadastro.pack(fill="x", padx=15, pady=10)

tk.Label(frame_cadastro, text="Nome do Produto:", bg=COR_FUNDO, fg=COR_LETREIRO, font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w", pady=2)
ent_nome = tk.Entry(frame_cadastro, width=35)
ent_nome.grid(row=0, column=1, pady=2, padx=5)

tk.Label(frame_cadastro, text="Preço (R$):", bg=COR_FUNDO, fg=COR_LETREIRO, font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="w", pady=2)
ent_preco = tk.Entry(frame_cadastro, width=35)
ent_preco.grid(row=1, column=1, pady=2, padx=5)

tk.Label(frame_cadastro, text="Qtd Estoque:", bg=COR_FUNDO, fg=COR_LETREIRO, font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="w", pady=2)
ent_estoque = tk.Entry(frame_cadastro, width=35)
ent_estoque.grid(row=2, column=1, pady=2, padx=5)

tk.Label(frame_cadastro, text="Validade (DD.MM.AAAA):", bg=COR_FUNDO, fg=COR_LETREIRO, font=("Arial", 10, "bold")).grid(row=3, column=0, sticky="w", pady=2)
ent_validade = tk.Entry(frame_cadastro, width=35)
ent_validade.grid(row=3, column=1, pady=2, padx=5)

tk.Label(frame_cadastro, text="Descrição:", bg=COR_FUNDO, fg=COR_LETREIRO, font=("Arial", 10, "bold")).grid(row=4, column=0, sticky="w", pady=2)
ent_desc = tk.Entry(frame_cadastro, width=35)
ent_desc.grid(row=4, column=1, pady=2, padx=5)

btn_salvar = tk.Button(frame_cadastro, text="Salvar Produto", command=cadastrar_produto_visual, bg=COR_BOTAO_BG, fg=COR_BOTAO_FG, font=("Arial", 10, "bold"), relief="raised", bd=2)
btn_salvar.grid(row=5, column=0, columnspan=2, pady=10)

# --- SEÇÃO 2: LANÇAR VENDA ---
frame_venda = tk.LabelFrame(scrollable_frame, text=" Lançar Venda ", font=("Arial", 11, "bold"), bg=COR_FUNDO, fg=COR_LETREIRO, padx=10, pady=10)
frame_venda.pack(fill="x", padx=15, pady=10)

tk.Label(frame_venda, text="Nome do Hambúrguer:", bg=COR_FUNDO, fg=COR_LETREIRO, font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w", pady=2)
ent_venda_nome = tk.Entry(frame_venda, width=35)
ent_venda_nome.grid(row=0, column=1, pady=2, padx=5)

tk.Label(frame_venda, text="Quantidade:", bg=COR_FUNDO, fg=COR_LETREIRO, font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="w", pady=2)
ent_venda_qtd = tk.Entry(frame_venda, width=35)
ent_venda_qtd.grid(row=1, column=1, pady=2, padx=5)

btn_vender = tk.Button(frame_venda, text="Confirmar Venda 🍔", command=realizar_venda_visual, bg=COR_BOTAO_BG, fg=COR_BOTAO_FG, font=("Arial", 10, "bold"), relief="raised", bd=2)
btn_vender.grid(row=2, column=0, columnspan=2, pady=10)

# --- SEÇÃO 3: CARDÁPIO / SITUAÇÃO DO ESTOQUE (FICA EMBAIXO) ---
frame_estoque = tk.LabelFrame(scrollable_frame, text=" Cardápio & Estoque Atual ", font=("Arial", 11, "bold"), bg=COR_FUNDO, fg=COR_LETREIRO, padx=10, pady=10)
frame_estoque.pack(fill="both", expand=True, padx=15, pady=10)

txt_lista = tk.Text(frame_estoque, height=10, width=58, font=("Courier New", 9, "bold"), bg="#FFFDE7", fg="#333333")
txt_lista.pack(pady=5)

btn_atualizar = tk.Button(frame_estoque, text="Atualizar Lista", command=atualizar_lista_visual, bg=COR_BOTAO_BG, fg=COR_BOTAO_FG, font=("Arial", 10, "bold"), relief="raised", bd=2)
btn_atualizar.pack(pady=5)

# Força a exibição inicial dos produtos cadastrados
atualizar_lista_visual()

# Inicia o loop do Tkinter
janela.mainloop()