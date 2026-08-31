# Essa função pega uma lista de números e retorna o maior e o menor numero dentro delas.
def maior_menor(lista_de_numeros):
  
    if not lista_de_numeros:
        return None, None 

   
    maior_valor = max(lista_de_numeros)
    menor_valor = min(lista_de_numeros)
    
   
    return maior_valor, menor_valor

# essa parte do código exibe a lista de numeros testando a função.
print("--- Teste com uma lista de números ---")
numeros = [12, 5, 25, 8, 17, 3, 30]
maior_valor, menor_valor = maior_menor(numeros)



print(f"A lista de números é: {numeros}")
print(f"O maior valor na lista é: {maior_valor}")
print(f"O menor valor na lista é: {menor_valor}")

print("\n--- Teste com uma lista vazia ---")
lista_vazia = []
maior_vazio, menor_vazio = maior_menor(lista_vazia)

print(f"A lista é: {lista_vazia}")
print(f"Maior valor: {maior_vazio}, Menor valor: {menor_vazio}")

