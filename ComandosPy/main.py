import json

try:
    with open("configuracoes.json", "r") as config:
        comandos = json.load(config)
except (FileNotFoundError, json.JSONDecodeError):
    comandos = []
            
def limpar():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
def salvar_configuracoes():
    with open("configuracoes.json" , "w") as config:
            json.dump(comandos, config)
    
def cadastrar_comando():
    
    while True:
        
        limpar()
            
        print("Cadastrar um comando: ")
        print("Você pode retornar ao menu inicial digitando 'sair' a qualquer momento.\n")
        
        nome = input("Digite o nome do comando: ")
        if nome.lower() == "sair":
            break
        elif not nome.strip():
            print("O nome não pode estar vazio.")
            input("Pressione ENTER...")
            continue
        
        descricao = input("Digite a descricao do comando: ")
        if descricao.lower() == "sair":
            break
        elif not descricao.strip():
            print("A descrição não pode estar vazia.")
            input("Pressione ENTER...")
            continue
        
        novo_id = len(comandos) + 1
        
        comando = {
            "id" : novo_id,
            "nome" : nome,
            "descricao" : descricao
        }
        
        comandos.append(comando)
        salvar_configuracoes()

        print("\nComando adicionado com sucesso!")
        escolha = input("Deseja adicionar outro comando? (s/n) ")
        if escolha != "s":
            break
        
def listar_comando():
    
    while True:
        
        limpar()
        
        print("Todos os comandos cadastrados: ")
        
        if not comandos:
            print("Nenhum comando cadastrado.")
        else:
            for comando in comandos:
                print(comando)      
            
        escolha = input("\nDigite 'sair' para retornar: ")  
        if escolha.lower() == "sair":
            break

def procurar_id_comando():
    
    while True:
        
        limpar()
        
        print("Buscar um comando:")
        print("Você pode retornar ao menu inicial digitando 'sair' a qualquer momento.\n")
        
        pesquisa = input("Digite o ID do comando para pesquisar: ")
        if pesquisa.lower() == "sair":
            break
        if not pesquisa.isdigit():
            print("\nDigite apenas números.")
            input("Pressione ENTER...")
            continue
        
        achado = None
        
        for comando in comandos:
            if comando["id"] == int(pesquisa):
                achado = comando
                break
            
        if achado:
            print("\nComando encontrado:\n")
            print(achado)
        
        else:
            print("\nComando não encontrado.")
            
        escolha = input("\nDeseja pesquisar novamente? (s/n) ").lower()
        if escolha != "s":
            break
        
def excluir_comando():
    
    while True:
        
        limpar()
        
        print("Excluir um comandos:")
        print("Você pode retornar ao menu inicial digitando 'sair' a qualquer momento.\n")
        
        excluir = input("Digite o ID do comando que deseja excluir: ")
        if excluir.lower() == "sair":
            break
        
        elif not excluir.isdigit():
            print("\nDigite apenas números.")
            input("Pressione ENTER...")
            continue

        achado = None
        
        for comando in comandos:
            if comando["id"] == int(excluir):
                achado = comando
                break
        
        if achado is None:
            print("\nID não encontrado.")
            input("Pressione ENTER...")
            continue
        
        comandos.remove(achado)
        
        numeragem = 1
        for comando in comandos:
            comando["id"] = numeragem
            numeragem += 1
            
        salvar_configuracoes()
        
        print("Comando Excluido!\n")
        
        escolha = input("Deseja excluir outro comando? (s/n) ").lower()
        if escolha != "s":
            break

def menu():
    
    while True:
        
        limpar()
        
        print("Bem vindo ao ComandosPy!\n")
        
        print("[1] - Cadastrar Comando.")
        print("[2] - Listar Comandos.")
        print("[3] - Procurar um Comando.")
        print("[4] - Excluir um comando.")
        print("[0] - Encerrar Programa.")
        
        escolha = input("\nDigite o numero da opção que deseja selecionar: ")
        
        if escolha == "1":
            cadastrar_comando()
        
        elif escolha == "2":
            listar_comando()
        
        elif escolha == "3":
            procurar_id_comando()
            
        elif escolha == "4":
            excluir_comando()
        
        elif escolha == "0":
            print("Obrigado por comandar!")
            break
        
        else:
            print("Por favor, digite uma opção valida...")
            input("Pressione ENTER...")

menu()