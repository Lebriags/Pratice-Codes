# Exercicio de hoje é determinar o maior numero dentro de uma lista
# Mas sem usar max, tudo na mão mesmo. 

lista_numeros = input("Digite uma lista de números separados por vírgula: ").split(",") # split aqui pra tirar os espaços e separar os numeros
lista_numeros = [int(num) for num in lista_numeros]  # Converte os elementos para inteiros

while len(lista_numeros) != 5:
    lista_numeros = input("Por favor, digite exatamente 5 numeros: ").split(",")
    lista_numeros = [int(num) for num in lista_numeros]    
                    
# Variavel que vai receber o numero maior pra printar depois.
maior = lista_numeros[0]
    
# A magica que percorre cada numero dentro da lista.
for numero in (lista_numeros):
    if int(numero) > int(maior): # Compara o numero percorrido na lista com o numero dentro da variavel maior
        maior = numero # Se o numero da lista for maior, ele entra na variavel maior
        
        # Se não for maior, dai ele manda o numero para as cucuias e passa para o proximo numero até finalizar a lista.

# Printa o numero maior dentro da lista.
print(maior)
        