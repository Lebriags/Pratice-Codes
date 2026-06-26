nomes = []
verificado = []

recebimento = input("Escreva os nomes separados por virgula: ").split(",")
nomes.extend(recebimento)

for i in nomes:
    
    quantidade = len(i) 
    if quantidade > 5:        
        verificado.append(i)
        
print(len(verificado))    