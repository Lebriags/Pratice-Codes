lista = []
multiplos = 0

receber = input("Digite a sequencia de numeros separados por virgula e sem espaço: ").split(",")
lista.extend(receber)

for numero in lista:
    if int(numero) % 3 == 0:
        multiplos += 1
    else:
        pass

print(multiplos)
        
        
