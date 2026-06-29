palavra = input("Por favor, informe a palavra: ")

contador_letra = 0

for letra in palavra:
    if letra == "a":
        contador_letra += 1
    elif letra == "A":
        contador_letra += 1    
    else:
        pass

print("Total de letras A: " , contador_letra)