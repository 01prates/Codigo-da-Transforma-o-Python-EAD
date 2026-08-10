def maior_menor(lista):
    maior = max(lista)
    menor = min(lista)
    return maior, menor

# Testando a função
meus_numeros = [15, 42, 8, 23, 99, 4, 16]
maior_val, menor_val = maior_menor(meus_numeros)

print(f"Lista original: {meus_numeros}")
print(f"Maior valor: {maior_val}")
print(f"Menor valor: {menor_val}")