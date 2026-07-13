frase = input("Escreva sua frase: ").split()

letras = frase[0]

for palavra in frase:
    
    if len(palavra) < len(letras):
        letras = palavra
    else:
        pass
    
print(letras)

