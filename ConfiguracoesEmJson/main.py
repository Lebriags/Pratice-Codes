import json

with open("configuracoes.json" , "r") as config:
    parametros = json.load(config)

def alterar_nome():
    
    while True:
               
        if parametros["Idioma"] == "Portugues":
        
            print("Alterar o nome de 'Alfredo'")
        
            resposta = input("Escreva o novo nome ou 'sair': ")
        
            if resposta == "sair":
                break
        
            parametros["Nome"] = resposta
            with open("configuracoes.json" , "w") as config:
                json.dump(parametros, config)
            print("Nome alterado para: " , parametros["Nome"])
            
        elif parametros["Idioma"] == "Ingles":
            
            print("Change the name of 'Alfredo'")
        
            resposta = input("Change the name or type 'exit': ")
        
            if resposta == "exit":
                break
        
            parametros["Nome"] = resposta      
            with open("configuracoes.json" , "w") as config:
                json.dump(parametros, config)
            print("Name changed to: " , parametros["Nome"])

def alterar_idioma():
    
    while True:
        
        if parametros["Idioma"] == "Portugues":
        
            print("Alterar o Idioma")
        
            print("[1] - Portugues BR")
            print("[2] - Inglês")
        
            resposta = input("Selecione o idioma ou 'sair': ")
        
            if resposta == "1":
                print("Idioma em portugues ja selecionado!")                
            elif resposta == "2":
                parametros["Idioma"] = "Ingles"
                with open("configuracoes.json" , "w") as config:
                    json.dump(parametros, config)
            elif resposta == "sair":
                break
        
        elif parametros["Idioma"] == "Ingles":
            
            print("Change the language")
        
            print("[1] - Portugues BR")
            print("[2] - English")
        
            resposta = input("Change the option language or type 'exit': ")
        
            if resposta == "2":
                print("Already done!")                
            elif resposta == "1":
                parametros["Idioma"] = "Portugues"
                with open("configuracoes.json" , "w") as config:
                    json.dump(parametros, config)
            elif resposta == "exit":
                break
            
def alterar_volume():
    
    while True:
        
        if parametros["Idioma"] == "Portugues":
            
            print("Altere o volume do som")
            
            resposta = input("Digite o volume desejado de 0 a 100: \nOu 'sair': ")
            if resposta == "sair":
                break
            
            elif resposta.isdigit() == False:
                print("Digite um numero, obviamente...")
                
            volume = int(resposta)
            
            if volume < 0:
                print("Digite um volume valido.")
            elif volume > 100:
                print("Vai estourar seus ouvidos!\nEscolha outro volume...")
            else:
                parametros["Volume"] = volume
                with open("configuracoes.json" , "w") as config:
                    json.dump(parametros, config)    
                
        if parametros["Idioma"] == "Ingles":
            
            print("Change de sound gain")
            
            resposta = input("Type the sound gain of 0 at 100: \nor 'exit': ")
            if resposta == "exit":
                break
            elif resposta.isdigit() == False:
                print("Type a number, obviously...")
                
            volume = int(resposta)
            
            if volume < 0:
                print("Type a valid sound gain.")
            elif volume > 100:
                print("It is blow up your ears!\nChoice other sound gain...")
            else:
                parametros["Volume"] = volume 
                with open("configuracoes.json" , "w") as config:
                    json.dump(parametros, config)

def modo_escuro():
    
    while True:
        
        if parametros["Idioma"] == "Portugues":
            
            print("Ativar modo escuro?")
            print("S ou N?")
            resposta = input("Aguardando resposta ou digite 'sair': ")
            
            if resposta.lower() == "s":
                parametros["Modo_escuro"] = "Ativado"
                print("Modo escuro ativado!")   
                with open("configuracoes.json" , "w") as config:
                    json.dump(parametros, config)             
            elif resposta.lower() == "n":
                parametros["Modo_escuro"] = "Desativado"
                with open("configuracoes.json" , "w") as config:
                    json.dump(parametros, config)
                print("Modo escuro desativado!")  
            elif resposta.lower() == "sair":
                break
                
            else:
                print("Resposta inválida.")
                
        elif parametros["Idioma"] == "Ingles":
            
            print("Enable dark mode?")
            print("Y or N?")
            resposta = input("Waiting for answer or type 'exit': ")
            
            if resposta.lower() == "y":
                parametros["Modo_escuro"] = "Enabled"
                with open("configuracoes.json" , "w") as config:
                    json.dump(parametros, config)
                print("Dark mode enabled!")   
            elif resposta.lower() == "n":
                parametros["Modo_escuro"] = "Disabled"
                with open("configuracoes.json" , "w") as config:
                    json.dump(parametros, config)
                print("Dark mode disabled!")                
            elif resposta.lower() == "exit":
                break
                
            else:
                print("Invalid answer.")

def configuracoes():
    
    while True:
        
        if parametros["Idioma"] == "Portugues":
            
            print("Configurações ativas: ")
            
            for chave, valor in parametros.items():
                
                print(f"{chave}: {valor}")

            resposta = input("Digite 'sair' para retornar ao menu: ")
            if resposta == "sair":
                break
            
        if parametros["Idioma"] == "Ingles":
            
            print("Active Settings: ")
            
            for chave, valor in parametros.items():
                
                print(f"{chave}: {valor}")

            resposta = input("Type 'exit' to return to main menu: ")
            if resposta == "exit":
                break

def menu():
    
    while True:
        
        if parametros["Idioma"] == "Portugues":
        
            print("Bem vindo ao Alfredo!\nEscolha uma das opções abaixo:")
        
            print("[1] - Alterar nome")
            print("[2] - Alterar Idioma")
            print("[3] - Alterar volume")
            print("[4] - Modo escuro")
            print("[5] - Mostrar configurações")
            print("[0] - Sair")
        
            escolha = input("Digite o numero da opção que deseja acessar: ")
        
            if escolha == "1":
                alterar_nome()
            
            elif escolha == "2":
                alterar_idioma()
        
            elif escolha == "3":
                alterar_volume()
            
            elif escolha == "4":
                modo_escuro()
        
            elif escolha == "5":
                configuracoes()
            
            elif escolha == "0":
                print("Obrigado por testar!")
                exit()
        
            else:
                print("Escolha uma opção valida.")
            
        elif parametros["Idioma"] == "Ingles":
        
            print("Welcome to Alfredo!\nChoice one option below:")
        
            print("[1] - Change name")
            print("[2] - Change Language")
            print("[3] - Sounds Options")
            print("[4] - Dark mode")
            print("[5] - Show Options allowed")
            print("[0] - Exit")
        
            escolha = input("Type the number of option to access: ")
        
            if escolha == "1":
                alterar_nome()
            
            elif escolha == "2":
                alterar_idioma()
        
            elif escolha == "3":
                alterar_volume()
            
            elif escolha == "4":
                modo_escuro()
        
            elif escolha == "5":
                configuracoes()
            
            elif escolha == "0":
                print("Thank you for testing!")
                exit()
        
            else:
                print("Type a valid option.")    
                
menu()