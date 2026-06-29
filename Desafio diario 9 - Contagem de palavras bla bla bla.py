lista = []

receber_lista = input("Escreva a lista de palavras separado por virgula e sem espaço: ").split(",")
lista.extend(receber_lista)

contagem_palavras = 0
contagem_cinco_letras = 0
contagem_vogal = 0

for palavra in lista:
    
    contagem_palavras += 1
    
    if len(palavra) > 5:
        contagem_cinco_letras += 1
        
    if palavra[0] not in ["a" , "A" , "e" , "E", "i", "I", "o", "O", "u" , "U"]:
        pass
    else:
        contagem_vogal += 1
        
print("Total de palavras: " , contagem_palavras)
print("Total de palavras com mais de 5 letras: " , contagem_cinco_letras)
print("Total de palavras que começam com uma vogal: " , contagem_vogal)        
