'''
um bloco de comentarios
>PO (como dono negocio) preciso de um sistema de vendas de hamburguer para que eu possa vender e lucrar

>QA (como cliente) preciso de um sistema facil de compras para que eu possa comprar de forma pratica

>tech (como progamador) quero um sistema que eu possa implementar funcionalidades basicas para atender o cliente 
de forma pratica 

>dev (como programador) quero um sistema facil e pratico de compras para minha hamburgueria para implementar as
funcionalidades a interface do sistema

>UX (como designer de experiencia do usuario) quero um sistema pratico e facil de usar para que o cliente possa comprar
 de forma pratica e rápida

>IA (como inteligencia artificial) quero um sistema de vendas de hamburguer para que o cliente possa comprar de forma pratica e rapida

'''

import tkinter as tk
from tkinter import messagebox, ttk

# --- VARIÁVEIS GLOBAIS (O modelo de dados baseado no do teu mentor) ---
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
    """Atualiza o texto da aba Cardápio com os dados atuais das variáveis."""
    txt_lista.delete('1.0', tk.END)
    global p1_nome, p2_nome, p3_nome
    
    if p1_nome == "" and p2_nome == "" and p3_nome == "":
        txt_lista.insert(tk.END, "Nenhum produto cadastrado no sistema ainda.")
        return
        
    if p1_nome != "":
        txt_lista.insert(tk.END, f"VAGA 1:\nNome: {p1_nome} | Preço: R$ {p1_preco:.2f} | Estoque: {p1_estoque} unid.\n")
        txt_lista.insert(tk.END, f"Validade: {p1_validade} | Descrição: {p1_descricao}\n")
        txt_lista.insert(tk.END, "🍔" * 35 + "\n\n")
        
    if p2_nome != "":
        txt_lista.insert(tk.END, f"VAGA 2:\nNome: {p2_nome} | Preço: R$ {p2_preco:.2f} | Estoque: {p2_estoque} unid.\n")
        txt_lista.insert(tk.END, f"Validade: {p2_validade} | Descrição: {p2_descricao}\n")
        txt_lista.insert(tk.END, "🍔" * 35 + "\n\n")
        
    if p3_nome != "":
        txt_lista.insert(tk.END, f"VAGA 3:\nNome: {p3_nome} | Preço: R$ {p3_preco:.2f} | Estoque: {p3_estoque} unid.\n")
        txt_lista.insert(tk.END, f"Validade: {p3_validade} | Descrição: {p3_descricao}\n")
        txt_lista.insert(tk.END, "🍔" * 35 + "\n\n")

def cadastrar_produto_visual():
    """Valida os dados inseridos e cadastra o hambúrguer numa vaga livre."""
    global p1_nome, p1_preco, p1_estoque, p1_validade, p1_descricao
    global p2_nome, p2_preco, p2_estoque, p2_validade, p2_descricao
    global p3_nome, p3_preco, p3_estoque, p3_validade, p3_descricao
    
    nome = ent_nome.get().strip()
    validade = ent_validade.get().strip()
    descricao = ent_desc.get().strip()
    
    if nome == "":
        messagebox.showwarning("Aviso", "O nome do produto não pode ficar em branco.")
        return

    # 1. Validação do Preço (Try/Except para evitar quebra com letras)
    try:
        preco = float(ent_preco.get())
        if preco <= 0:
            messagebox.showerror("Erro", "O preço deve ser maior que zero!")
            return
    except ValueError:
        messagebox.showerror("Erro", "Preço inválido! Digite apenas números (Ex: 25.90).")
        return

    # 2. Validação do Estoque
    try:
        estoque = int(ent_estoque.get())
        if estoque < 0:
            messagebox.showerror("Erro", "A quantidade de estoque não pode ser negativa!")
            return
    except ValueError:
        messagebox.showerror("Erro", "Estoque inválido! Digite um número inteiro.")
        return

    # 3. Validação da Data (Regra: Máx dia 31, Máx mês 12, Ano livre)
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
        messagebox.showerror("Erro", "Data inválida! Use o formato DD.MM.AAAA\n(Máximo: Dia 31, Mês 12).")
        return

    # Verificação de vagas disponíveis
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

    # Limpar campos após o sucesso
    ent_nome.delete(0, tk.END)
    ent_preco.delete(0, tk.END)
    ent_estoque.delete(0, tk.END)
    ent_validade.delete(0, tk.END)
    ent_desc.delete(0, tk.END)
    atualizar_lista_visual()

def realizar_venda_visual():
    """Realiza a venda atualizando o estoque das variáveis globais."""
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

    # Lógica de processamento da venda
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
janela.geometry("500x550")

# Criação das abas visuais (Notebook)
notebook = ttk.Notebook(janela)
aba_listar = ttk.Frame(notebook)
aba_cadastrar = ttk.Frame(notebook)
aba_venda = ttk.Frame(notebook)

notebook.add(aba_listar, text="Cardápio / Início")
notebook.add(aba_cadastrar, text="Cadastrar Hambúrguer")
notebook.add(aba_venda, text="Lançar Venda")
notebook.pack(expand=True, fill="both", padx=10, pady=10)

# --- LAYOUT: ABA LISTAR ---
lbl_boas_vindas = tk.Label(aba_listar, text="Hamburgueria Sampaio", font=("Arial", 14, "bold"), fg="#D32F2F")
lbl_boas_vindas.pack(pady=10)

txt_lista = tk.Text(aba_listar, height=16, width=55, font=("Arial", 10))
txt_lista.pack(pady=5)

btn_atualizar = tk.Button(aba_listar, text="Atualizar Lista", command=atualizar_lista_visual, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
btn_atualizar.pack(pady=5)

# --- LAYOUT: ABA CADASTRAR ---
tk.Label(aba_cadastrar, text="Nome do Produto:").pack(anchor="w", padx=40, pady=2)
ent_nome = tk.Entry(aba_cadastrar, width=40)
ent_nome.pack(padx=40, pady=2)

tk.Label(aba_cadastrar, text="Preço do Produto (R$):").pack(anchor="w", padx=40, pady=2)
ent_preco = tk.Entry(aba_cadastrar, width=40)
ent_preco.pack(padx=40, pady=2)

tk.Label(aba_cadastrar, text="Quantidade no Estoque:").pack(anchor="w", padx=40, pady=2)
ent_estoque = tk.Entry(aba_cadastrar, width=40)
ent_estoque.pack(padx=40, pady=2)

tk.Label(aba_cadastrar, text="Validade do Produto (ex: 23.04.2027):").pack(anchor="w", padx=40, pady=2)
ent_validade = tk.Entry(aba_cadastrar, width=40)
ent_validade.pack(padx=40, pady=2)

tk.Label(aba_cadastrar, text="Descrição do Produto:").pack(anchor="w", padx=40, pady=2)
ent_desc = tk.Entry(aba_cadastrar, width=40)
ent_desc.pack(padx=40, pady=2)

btn_salvar = tk.Button(aba_cadastrar, text="Salvar Produto", command=cadastrar_produto_visual, bg="#1976D2", fg="white", font=("Arial", 11, "bold"))
btn_salvar.pack(pady=20)

# --- LAYOUT: ABA VENDA ---
tk.Label(aba_venda, text="Nome do Hambúrguer para Venda:", font=("Arial", 11)).pack(anchor="w", padx=40, pady=10)
ent_venda_nome = tk.Entry(aba_venda, width=38, font=("Arial", 11))
ent_venda_nome.pack(padx=40, pady=5)

tk.Label(aba_venda, text="Quantidade a Vender:", font=("Arial", 11)).pack(anchor="w", padx=40, pady=10)
ent_venda_qtd = tk.Entry(aba_venda, width=38, font=("Arial", 11))
ent_venda_qtd.pack(padx=40, pady=5)

btn_vender = tk.Button(aba_venda, text="Confirmar Venda 🍔", command=realizar_venda_visual, bg="#E64A19", fg="white", font=("Arial", 12, "bold"))
btn_vender.pack(pady=35)

# Força a exibição inicial dos produtos cadastrados por padrão
atualizar_lista_visual()

# Inicia o loop do Tkinter para manter a janela aberta
janela.mainloop()