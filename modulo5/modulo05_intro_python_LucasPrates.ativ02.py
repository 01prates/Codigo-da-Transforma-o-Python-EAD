def ler_nota_valida(ordem_nota):
    while True:
        entrada = input(f"Digite a {ordem_nota}ª nota (1 a 10): ").strip()
        # Substitui a vírgula por ponto para o Python conseguir converter
        entrada_com_ponto = entrada.replace(',', '.')
        
        try:
            nota = float(entrada_com_ponto)
            if 1.0 <= nota <= 10.0:
                return nota
            else:
                print("❌ Nota inválida! Digite um valor entre 1 e 10.")
        except ValueError:
            print("❌ Entrada inválida! Digite apenas números.")

def calcular_media(nota1, nota2, nota3, nota4):
    media = (nota1 + nota2 + nota3 + nota4) / 4
    
    print(f"\nMédia final: {media:.2f}".replace('.', ','))
    
    if media < 5.0:
        print("Status: NOTA VERMELHA (Reprovado) ❌")
    else:
        print("Status: APROVADO! 📊")

# --- Entrada dos dados com validação ---
n1 = ler_nota_valida(1)
n2 = ler_nota_valida(2)
n3 = ler_nota_valida(3)
n4 = ler_nota_valida(4)

# Chamada da função
calcular_media(n1, n2, n3, n4)