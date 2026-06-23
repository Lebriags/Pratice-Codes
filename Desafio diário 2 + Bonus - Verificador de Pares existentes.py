# O classico identificador de Par ou Impar. 
# Testa ai...

identificador = input("Digite o identificador (ou 'sair' para encerrar): ")
Par = 0

if identificador.lower() == 'sair':
    print("Encerrando o programa.")
    exit() 
   
for i in range(1, int(identificador) + 1):
    if i % 2 == 0:
        Par += 1
        
print(Par)

------------------------------------------------------------------------------------------------------

# É só descomentar essa parte para rodar o código, mas não esquece de comentar o de cima se não da merda.
# To começando a me acostumar mais com esse lance de programar então esse Bonus aqui foi mais facil.

'''recebimento = input("Digite a palavra (ou 'sair' para encerrar): ")
if recebimento.lower() == 'sair':
    exit()
    
vogais = 0

for Letra in recebimento:
    if Letra.lower() in 'aeiou':
        vogais += 1      
        
print(vogais)'''
