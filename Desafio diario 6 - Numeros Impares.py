lista = []

numero_recebido = input("Digite a sequencia de numeros: ").split(",")
lista.extend(numero_recebido)

impares = 0

for i in lista:
    if int(i) % 2 == 1:
        impares += 1
    else:
        pass

print("Os total de numeros impares são" , impares)        
