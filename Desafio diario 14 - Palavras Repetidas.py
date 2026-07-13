lista = input("Digite sua lista de palavras separadas por virgula: ").split(",")

repetidas = 0
apareceu = []

for palavra in lista:
    
    if palavra not in apareceu:
        apareceu.append(palavra)
        
        if lista.count(palavra) > 1:
            repetidas += 1

print(repetidas)
    