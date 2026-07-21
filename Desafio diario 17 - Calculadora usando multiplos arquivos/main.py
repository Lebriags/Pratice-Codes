from utilitarios import limpar, menu_somar, menu_subtrair, menu_multiplicar, menu_dividir

def menu():
    
    while True:
        
        limpar()
        
        print("Calculadora usando multiplos arquivos:\n")
        
        print("[1] - Somar")
        print("[2] - Subtrair")
        print("[3] - Multiplicar")
        print("[4] - Dividir\n")
        
        print("[0] - Encerrar programa\n")
        
        escolha = input("Selecione o numero da opção desejada: ")
        
        if escolha == "1":
            menu_somar()
        
        elif escolha == "2":
            menu_subtrair()
        
        elif escolha == "3":
            menu_multiplicar()
        
        elif escolha == "4":
            menu_dividir()
        
        elif escolha == "0":
            limpar()
            print("Obrigado por calcular!\n")
            break
        
        else:
            print("Digite uma opção valida...")
            input("Press ENTER...")
            continue

menu()        