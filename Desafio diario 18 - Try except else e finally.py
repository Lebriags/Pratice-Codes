# O try
# sintax:
'''try:
    escolha = float(input("Escreva um numero: "))
    print(escolha)
except:
    pass '''

''' O try é usado somente em espaços no código que possam gerar erros, ou melhor dizendo, exceções.
    O que esse trecho diz é: "Tente executar isso" E logo depois vem a exeção ou o tratamendo de erro que esse código pode gerar'''
    
# Except
# sintax:
'''try:
    escolha = float(input("Escreva um numero: "))
    print(escolha)
except ValueError:
    print("Digite apenas numeros.") '''
    
''' O except é o tratamento de erro em si,
    ao inves de só crashar o programa e fechar tudo, o except permite que o programa continue rodando. 
    Há varios tipos de exceções. '''
    
# A seguir, um pequeno menu de exemplos de Try, except, else e finally:

while True:
    
    print("Execute o programa com o código aberto para acompanhar o que esta acontecendo...\n")
    print("Menu de estudos e laboratório de vizualização:")
    
    print("\n[1] - VallueError")
    print("[2] - TypeError")
    print("[3] - ZeroDivisionError")
    print("[4] - FileNotFoundError")
    print("[5] - Else")
    print("[6] - Finally")
    
    print("[0] - Fechar Laboratorio\n")
    
    escolha = input("Digite uma opção: ")
    
    if escolha == "1":      
        try:
            receber_numero = float(input("Digite um numero: "))
            print(receber_numero)
        except ValueError:
            print("Por favor, digite apenas numeros!")
            input("...")
            
    elif escolha == "2":
        try:
            palavra = 100
            print(len(palavra))
        except TypeError:
            print("Um len precisa de algo com comprimento para ler, numeros não possuem isso.")
            print("Multiplicar str com int gera erro de tipos também.")
            print("Existem varios tipos de TypeError, mas são casos bem especificos.")
            input("...")
    
    elif escolha == "3":
        try:
            divisão = 0 / 0
            print(divisão)
        except ZeroDivisionError:
            print("É impossivel dividir por zero!")
            input("...")
    
    elif escolha == "4":
        try:
            with open("budega.json" , "r") as bd:
                vizualizar = bd.read()
            print(vizualizar)
        except FileNotFoundError:
            print("Arquivo inexistente ou não encontrado.")
            input("...")
    
    elif escolha == "5":
        try:
            escala = float(input("Escreva um numero de 0 a 10: "))
            if escala > 10:
                print("Somente entre 0 a 10")
            elif escala <= 5:
                print("Você é chato!" , escala)
            elif escala > 6:
                print("Voce é legal!" , escala)
        except ValueError:
            print("Digite somente numeros") 
        else:
            print("Escala feita com sucesso!")
            input("...")
    
    elif escolha == "6":
        try:
            numero = float(input("Escolha um numero para ser divisor: "))
            divisao = 100 / numero
        except ValueError:
            print("Somente numeros!")
        except ZeroDivisionError:
            print("Não divida por zero!")
        else:
            print(f"seu resultado: {divisão}")
        finally: 
            print("Operação encerrada...")
            input("...")
    
    elif escolha == "0":
        print("É isso...")
        break
    
    else:
        print("Digite uma opção valida!")
        input("Press ENTER... ")