# Pensamento_computacional_projeto
primeiro repertorio para praticas de versionamento de gihub e prompt de comando

# 🍔 Sistema de Vendas e Estoque - Hamburgueria Sampaio (GUI)

Este projeto consiste em um **Sistema de Gestão de Vendas e Estoque** desenvolvido em **Python** utilizando a biblioteca gráfica **Tkinter (GUI)**. O sistema permite cadastrar produtos, visualizar o cardápio com atualização em tempo real e realizar vendas com controle automático de estoque.

---

## 👥 Visão Geral e Papéis do Projeto

O desenvolvimento deste software levou em consideração diferentes perspectivas e papéis dentro de um projeto de tecnologia:

- **PO (Dono do Negócio):** Controle centralizado dos preços, limite de vagas e baixa automática no estoque.
- **QA (Testador / Qualidade):** Validação de entradas (datas, valores numéricos e campos obrigatórios) para garantir estabilidade.
- **Tech / Dev (Programador):** Estrutura funcional visual moderna, manutenível e responsiva via `Tkinter`.
- **UX (Designer):** Interface temática estilizada nas cores do estabelecimento, com suporte a rolagem gráfica (`Scrollbar`).
- **IA / Dados:** Base para captura e estruturação de histórico de movimentação de produtos.

---

## 🔄 Ciclo de Vida do Desenvolvimento

1. **Planejamento:** Definição dos requisitos do sistema de vendas e regra de cadastro limitado.
2. **Análise de Requisitos:** Regras de validação (preço positivo, datas `DD.MM.AAAA`, estoque positivo).
3. **Desenvolvimento Visual:** Construção da interface rica em Python via `Tkinter` e `ttk`.
4. **Testes de Campo:** Validação de conversão de dados e tratamento de erros com alertas nativos (`messagebox`).
5. **Implantação:** Disponibilização da interface para uso em ponto de venda (PDV).
6. **Manutenção:** Ajustes de layout e preparação para refatoração orientada a objetos (POO) e bancos de dados.

---

## 🚀 Funcionalidades do Sistema

- **📌 Cadastrar Novo Hambúrguer:**
  - Validação rigorosa de nome, preço, estoque e formato de validade (`DD.MM.AAAA`).
  - Suporte a até 3 vagas/produtos ativos simultaneamente no sistema.
- **🍔 Lançar Venda:**
  - Busca de produtos sem distinção entre maiúsculas e minúsculas (*case-insensitive*).
  - Verificação de disponibilidade e cálculo imediato do valor total da venda.
  - Abatimento automático na quantidade em estoque.
- **📋 Cardápio & Estoque Atual:**
  - Exibição dinâmica e formatada de todos os produtos cadastrados.
  - Botão de atualização rápida do painel visual.
- **📜 Interface com Rolagem:**
  - Suporte a `Canvas` + `Scrollbar` para navegação fluida em telas de diferentes resoluções.

---

## 🛠️ Tecnologias e Conceitos Utilizados

- **Linguagem:** Python 3
- **Interface Gráfica (GUI):** `tkinter`, `tkinter.ttk`, `tkinter.messagebox`
- **Tratamento de Exceções:** Blocos `try / except (ValueError)` para impedir inserção de dados inválidos.
- **Validação de Strings e Datas:** Métodos `.strip()`, `.split()`, e verificações lógicas de calendário.
- **Gerenciadores de Layout:** `pack()` e `grid()` para componentes organizados.

---

## 💻 Como Executar a Aplicação

### Pré-requisitos
- **Python 3.x** instalado. (A biblioteca `Tkinter` já vem inclusa por padrão na instalação do Python para Windows/macOS).

### Passo a Passo

1. **Clonar ou Baixar o Repositório:**
   Salve o script Python (ex: `app_hamburgueria.py`) e o arquivo `README.md` na mesma pasta.

2. **Abrir o Terminal / Prompt de Comando:**
   Navegue até a pasta onde o arquivo foi salvo:
   ```bash
   cd caminho/da/sua/pasta