# ==============================================================================
# ATIVIDADE 1: Operadores Aritméticos
# Objetivo: Criar programas (ou funções) que realizam as operações básicas.
# ==============================================================================

print("--- Exercício 1: Operadores Aritméticos ---")

# Pedindo os dois números para o usuário
# Usamos 'float' para que o programa aceite números com vírgula (pontos decimais)
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))


soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

if num2 != 0:
    divisao = num1 / num2
    resto = num1 % num2
else:
    divisao = "Não é possível dividir por zero!"
    resto = "Não é possível calcular o resto de uma divisão por zero!"

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Resto da divisão: {resto}")
print("-" * 40)