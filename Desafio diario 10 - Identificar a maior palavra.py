lista = []

receber_lista = input("Digite as palavras separadas por virgula e sem espaços: ").split(",")
lista.extend(receber_lista)

maior_palavra = ""

for palavra in lista:
    if len(palavra) > len(maior_palavra):
        maior_palavra = palavra 

print("A maior palavra é: " , maior_palavra)        