import utilidades

# Executando as funções do módulo utilidades
num1 = 10
num2 = 5

resultado_soma = utilidades.somar(num1, num2)
resultado_sub = utilidades.subtrair(num1, num2)
resultado_pot = utilidades.potencia(num1, 2)

print(f"Soma de {num1} + {num2} = {resultado_soma}")
print(f"Subtração de {num1} - {num2} = {resultado_sub}")
print(f"Potência de {num1} ao quadrado = {resultado_pot}")