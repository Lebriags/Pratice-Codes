Tarefa = []

while True:
    
    print("Bem vindo ao ToList!")
    
    print("Escolha uma opção:")
    print("[1] - Adicionar Tarefa.")
    print("[2] - Listar Tarefas.")
    print("[3] - Concluir Tarefa.")
    print("[4] - Quantidade de Tarefas.")
    print("[5] - Encerrar Programa.")
    
    escolha = input("Sua opção: ")
    
    if escolha == "1":
        
        while True:
            
            contador = len(Tarefa) + 1
            
            print("Adicionar uma Tarefa.")
            adicionar = input("Digite o nome da tarefa ou 'retornar': ")
            
            if adicionar == "retornar":
                break
            elif adicionar == "":
                print("Por favor, digite uma tarefa.")
            else: 
                nova_tarefa = [contador, adicionar, "Pendente" ]
                Tarefa.append(nova_tarefa)
                print("Tarefa adicionada")
    
    elif escolha == "2":
        
        while True:
            print("Tarefas existentes:")
            print(Tarefa)
        
            voltar = input("Para retornar ao menu, digite 'retornar': ")
        
            if voltar == "retornar":
                break
            elif voltar != "retornar":
                print("Digite 'retornar', por favor.")
            
    elif escolha == "3":
        
        while True:
            
            print("Concluir Tarefas.")
            concluir = input("Digite o numero da Tarefa para concluir ou 'retornar' para voltar ao menu: ")
            
            if concluir == "retornar":
                break
            elif concluir == "":
                print("Digite o numero de uma tarefa.")
            for i in Tarefa:
                if int(concluir) == i[0]:
                    
                    i[2] = "Concluido"
                
                    print("Tarefa Concluida")   
                    break           
    
    elif escolha == "4":
        
        while True:
                
            pendentes = 0 
            concluidos = 0
                        
            print("Total de tarefas: " , len(Tarefa))
                
            for i in Tarefa:
                
                if i[2] == "Pendente":
                    pendentes += 1
                elif i[2] == "Concluido":
                    concluidos += 1
                        
            print("Total de tarefas pendentes: " , pendentes)
            print("Total de tarefas concluidas: " , concluidos)        
            retornar = input("Para retornar ao menu, digite 'retornar': ")
            if retornar == "retornar":
                break
            elif retornar != "retornar":
                print("Por favor, digite 'retornar.")
                    
    elif escolha == "5":
        print("Obrigado por usar ToList!")
        exit()
        
    elif escolha not in ["1", "2", "3", "4", "5"]:
        print("Opção invalida!")