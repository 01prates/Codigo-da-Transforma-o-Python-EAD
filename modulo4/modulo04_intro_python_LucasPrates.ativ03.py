# Conjunto/Lista de números fornecido
numeros = [12, 7, 5, 18, 22, 9, 3, 14, 30, 11]

pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("=== CLASSIFICAÇÃO DE NÚMEROS ===")
print(f"Todos os números: {numeros}")
print(f"Números Pares:    {pares}")
print(f"Números Ímpares:  {impares}")