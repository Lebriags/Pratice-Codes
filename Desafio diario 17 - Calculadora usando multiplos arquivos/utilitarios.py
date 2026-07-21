from operacoes import somar, subtrair, multiplicar, dividir

def limpar(): 
    import os 
    os.system('cls' if os.name == 'nt' else 'clear')
    
def menu_somar():
    
    while True:
        
        limpar()
        
        print("Somar numeros!\n")
        print("Você pode retornar ao menu a qualquer momento pressionando ENTER no campo vazio...\n")
        
        resposta1 = input("Digite o primeiro numero: ")
        if resposta1 == "":
            break
        num1 = float(resposta1)
        
        resposta2 = input("Digite o segundo numero: ")
        if resposta2 == "":
            break
        num2 = float(resposta2)
        
        resultado = somar(num1, num2)
        print(f"\nO resultado da soma é: {resultado}!")
        
        resposta = input("Deseja somar novamente? (s/n)").lower()
        if resposta != "s":
            break
        else:
            continue

def menu_subtrair():
    
    while True:
        
        limpar()
        
        print("Subtrair numeros!\n")
        print("Você pode retornar ao menu a qualquer momento pressionando ENTER no campo vazio...\n")
        
        resposta1 = input("Digite o primeiro numero: ")
        if resposta1 == "":
            break
        num1 = float(resposta1)
        
        resposta2 = input("Digite o segundo numero: ")
        if resposta2 == "":
            break
        num2 = float(resposta2)
        
        resultado = subtrair(num1, num2)
        print(f"\nO resultado da subtração é: {resultado}!")
        
        resposta = input("Deseja subtrair novamente? (s/n)").lower()
        if resposta != "s":
            break
        else:
            continue

def menu_multiplicar():
    
    while True:
        
        limpar()
        
        print("Multiplicar numeros!\n")
        print("Você pode retornar ao menu a qualquer momento pressionando ENTER no campo vazio...\n")
        
        resposta1 = input("Digite o primeiro numero: ")
        if resposta1 == "":
            break
        num1 = float(resposta1)
        
        resposta2 = input("Digite o segundo numero: ")
        if resposta2 == "":
            break
        num2 = float(resposta2)
        
        resultado = multiplicar(num1, num2)
        print(f"\nO resultado da multiplicação é: {resultado}!")
        
        resposta = input("Deseja multiplicar novamente? (s/n)").lower()
        if resposta != "s":
            break
        else:
            continue

def menu_dividir():
    
    while True:
        
        limpar()
        
        print("Dividir numeros!\n")
        print("Você pode retornar ao menu a qualquer momento pressionando ENTER no campo vazio...\n")
        
        resposta1 = input("Digite o primeiro numero: ")
        if resposta1 == "":
            break
        num1 = float(resposta1)
        
        resposta2 = input("Digite o segundo numero: ")
        if resposta2 == "":
            break
        num2 = float(resposta2)
        
        resultado = dividir(num1, num2)
        print(f"\nO resultado da divisão é: {resultado}!")
        
        resposta = input("Deseja dividir novamente? (s/n)").lower()
        if resposta != "s":
            break
        else:
            continue
