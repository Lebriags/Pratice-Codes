Lista = []

receber = input("Digite a sequencia de numeros: ").split(",")

Lista.extend(receber)

maior = int(Lista[0])
menor = int(Lista[0]) 
soma = 0
pares = 0

for numero in Lista:
    soma += int(numero)
    
    if int(numero) > int(maior):
        maior = numero
    elif int(numero) < menor:
        menor = numero

    if int(numero) % 2 == 0:
        pares += 1
    
print("Maior: ", maior, "\nMenor: ", menor, "\nSoma: ", soma, "\nPares: ", pares)
    
        