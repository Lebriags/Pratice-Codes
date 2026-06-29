lista = []

receber_numero = input("Adicione numeros separados por virgula sem espaço: ").split(",")
lista.extend(receber_numero)

soma_total = 0

for i in lista:
    i = int(i)
    if i > 0:
        soma_total += i
    
print(soma_total)
        