funcionarios = []

while True:
    print("Bem vindo ao CadFuncionarios!")
    print("Para selecionar uma opção, basta digitar o numero correspondente a ela")
    print("[1] - Cadastrar Funcionário")
    print("[2] - Listar Funcionários")
    print("[3] - Procurar Funcionario")
    print("[4] - Quantidade de Funcionarios Cadastrados")
    print("[5] - Fechar Programa")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
        
        while True: 
            
            print("Cadastro de funcionario")
            print("Para retornar a opção anteriror, digite 'retornar'.")
            cadastro = input("Por favor, digite: 'nome', 'idade', 'cargo' sem espaços: ").split(",")
        
            if cadastro == ["retornar"]:
                break
            elif len(cadastro) != 3:
                print("Por favor, digite um cadastro valido.")
            elif cadastro[0] == "":
                print("Por favor, digite um cadastro valido.")
            elif cadastro[2] == "":
                print("Por favor, digite um cadastro valido.")
            elif not cadastro[1].isdigit():
                print("Por favor, digite um cadastro valido.")
            else:
                funcionarios.append(cadastro)
                print("Funcionario cadastrado com sucesso!")
                
    elif escolha == "2":
        print("Lista de Funcionarios atualizada:")
        
        while True:
            
            for i in funcionarios:
                print(i)
            if funcionarios == []:
                print("Sem funcionarios cadastrados.")
                        
            cadastro = input("Para voltar ao menu, digite 'retornar': ")
            if cadastro.lower() == "retornar":
                break

    elif escolha == "3":
        print("Procurar funcionario!")
        while True:
            
            print("Para voltar ao menu, digite 'retornar'.")
            pesquisa = input("Digite o nome do funcionario: ").lower()
            if pesquisa == "retornar":
                break
            elif pesquisa == "":
                print("Por favor, digite um nome.")
            encontrado = False

            for p in funcionarios:
                if pesquisa == p[0]:
                    print("Aqui esta seu funcionario!")
                    print(p)
                    encontrado = True

            if not encontrado:
                print("Acho que você errou o nome do funcionario.")
    
    elif escolha == "4":
        
        while True:
            print("Quantidade total de funcionarios: ")
    
            print(len(funcionarios))
            if funcionarios == []:
                print("sem funcionarios cadastrados")
            
            retorno = input("Para retornar ao menu, digite 'retornar': ")
            if retorno == "retornar":
                break
                       
    elif escolha == "5":
        print("Obrigado por usar!")
        exit()
        
    elif escolha not in ["1", "2", "3", "4", "5"]:
        print("Opção invalida!")
    