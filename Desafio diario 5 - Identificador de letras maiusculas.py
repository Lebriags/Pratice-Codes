palavra = input("Escreva sua palavra aqui: ")
letrasmaiusculas = 0

for letra in palavra:
    
    if letra.isupper():
    
        letrasmaiusculas += 1
    
print(letrasmaiusculas)    