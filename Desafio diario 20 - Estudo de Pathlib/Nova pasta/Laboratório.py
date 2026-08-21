from pathlib import Path

def Verificar_Diretorio_Base_Atual():
    
    while True:
        
        print("\n[1] - Mostrar Diretorio que você esta")
        print("[2] - Mostrar Diretorio base")
        
        escolha = input("\nSelecione uma opção (Ou pressione enter para voltar ao menu anterior): ")
        
        if escolha == "1":
            diretorio_atual = Path.cwd()
            print(f"\nVocê esta em: \n{diretorio_atual} \n")
        
        elif escolha == "2":
            diretorio_base = Path.home()
            print(f"\nSeu diretório base é: \n{diretorio_base} \n")
            
        elif escolha == "":
            print("\nVoltando...")
            break
            
        elif escolha not in ["1", "2"]:
            print("\nPor favor, selecione uma opção valida")

def Informacoes_Diretorio():
    
    while True: 
        
        diretorio = Path.cwd()
        print(f"\nInformações sobre esse diretório: \n{diretorio}\n")
        
        print("[1] - Saber se ele existe")
        print("[2] - Saber se é um arquivo")
        print("[3] - Saber se é um diretório")
        print("[4] - Qual o nome")
        print("[5] - Qual a extensão")
        print("[6] - Qual o nome sem a extensão")
        print("[7] - QUal o diretório pai\n")
        
        escolha = input("Digite a opção da informação que deseja verificar (Ou ENTER para sair): ")
        
        if escolha == "1":
            if diretorio.exists():
                print("\nSim, ele existe.")
            else:
                print("\nNão existe.")
          
        elif escolha == "2":
            if diretorio.is_file():
                print("\nSim, é arquivo.")
            else:
                print("\nNão é arquivo.")
                
        elif escolha == "3":
            if diretorio.is_dir():
                print("\nSim, é diretório.")
            else:
                print("\nNão é diretório.")
        
        elif escolha == "4":
            if diretorio.exists():
                print(f"\nNome é: {diretorio.name}")
            else:
                print("\nNão existe esse arquivo ou diretório")
        
        elif escolha == "5":
            if diretorio.is_file():
                print(f"\nExensão é: {diretorio.suffix}")
            elif diretorio.exists() == False:
                print("\nEsse diretório ou arquivo não existe.")
            else:
                print("\nNão é um arquivo para mostrar  extensão.")
                
        elif escolha == "6":
            if diretorio.exists():
                print(f"\nNome sem extensão é: {diretorio.stem}")
            elif diretorio.is_file() == False:
                print("\nNão tem pra que mostrar o nome sem extensão se ele é uma pasta.")
            else:
                print("\nNão existe esse arquivo ou diretório")
        
        elif escolha == "7":
            if diretorio.exists():
                print(f"\nDiretório pai é: {diretorio.parent}")
            else:
                print("\nNão existe esse arquivo ou diretório")
        
        elif escolha == "":
            print("\nVoltando...\n")
            break
        
        elif escolha not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("\nEscolha uma opção valida.")
            
def Explorar_Diretorio():
    
    while True:
        
        listar_diretorio = Path.cwd()
        
        print("\nTudo o que há no diretório: \n")
        
        for item in listar_diretorio.iterdir():
            if item.is_file():
                print("[ARQUIVO] " , item.name)
            elif item.is_dir():
                print("[PASTA] " , item.name)
        
        input("\nDigite ENTER para retornar... ")
        print("Retornando...\n")
        break

def Filtrar_Arquivos():
    
    while True:
        
        count_pdf = 0
        count_py = 0
        count_jpg = 0
        
        diretorio = Path.cwd()
        
        print("\nFiltrar por tipo de arquivo: \n")
        
        print("[1] - .py")
        print("[2] - .pdf")
        print("[3] - .jpg")
        
        escolha = input("\nDigite a opção que queira filtrar (Ou ENTER para voltar): ")
        
        if escolha == "1":
            for item in diretorio.glob("*.py"):
                if item.suffix == ".py":
                    print(item.name)
                    count_py += 1
            if count_py <= 0:
                print("Sem arquivos .py")            
        
        elif escolha == "2":
            for item in diretorio.glob("*.pdf"):
                if item.suffix == ".pdf":
                    print(item.name)
                    count_pdf += 1
            if count_pdf <= 0:
                print("Sem arquivos .pdf")
                
        elif escolha == "3":
            for item in diretorio.glob("*.jpg"):
                if item.suffix == ".jpg":
                    print(item.name)
                    count_jpg += 1
            if count_jpg <= 0:
                print("Sem arquivos .jpg") 

        elif escolha == "":
            print("\nVoltando... \n")
            break
        
        elif escolha not in ["1" , "2" , "3"]:
            print("Selecione uma opção valida")   

def Arvore_Diretorios():
    
    while True:
        
        print("\nArvore de diretórios: \n")
        
        diretorio = [
            Path("Laboratorio\\documentos"),
            Path("Laboratorio\\imagens"),
            Path("Laboratorio\\dados"),
            Path("Laboratorio\\temporarios")
        ]
        for diretorios in diretorio:
            diretorios.mkdir(parents=True, exist_ok=True)
            
            print(diretorios)
        
        input("\nPressione ENTER para voltar...")
        break
    
def Estatisticas():
    
    while True: 
        
        print("\nEstatisticas:\n")
        
        count_arquivos = 0
        count_pastas = 0
        count_extensoes = set()
        maior_arquivo = ""
        menor_arquivo = ""
    
        max_tamanho = 0
        min_tamanho = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        
        diretorio = Path.cwd()
        for item in diretorio.iterdir():
            if item.is_file():
                count_arquivos +=1
                count_extensoes.add(item.suffix)
                if item.stat().st_size >= max_tamanho:
                    max_tamanho = item.stat().st_size
                    maior_arquivo = item.name
                elif item.stat().st_size <= min_tamanho:
                    min_tamanho = item.stat().st_size
                    menor_arquivo = item.name
            elif item.is_dir():
                count_pastas += 1
        
        print("Quantidade de arquivos: " , count_arquivos)
        print("Quantidade de pastas: " , count_pastas)
        print("Extensoes no diretório: " , count_extensoes)
        print("Maior arquivo: " , maior_arquivo)
        print("Menor Arquivo: " , menor_arquivo)
        
        input("\nPressione ENTER para retornar.")
        break
            
while True:
    
    print("Janela de configurações para estudo do Pathlib\n")
    
    print("[1] - Verificar diretório base e onde você esta agora.")
    print("[2] - Informações sobre um diretório")
    print("[3] - Listar itens em diretório")
    print("[4] - Filtrando tipos de arquivos dentro de um dir")
    print("[5] - Mostrar Arvore de diretórios")
    print("[6] - Estatisticas do diretório")
    
    escolha = input("\nDigite uma opção (Ou apenas pressione ENTER para fechar o programa): ")
    
    if escolha == "1":
        Verificar_Diretorio_Base_Atual()
    
    elif escolha == "2":
        Informacoes_Diretorio()
        
    elif escolha == "3":
        Explorar_Diretorio()
        
    elif escolha == "4":
        Filtrar_Arquivos()
        
    elif escolha == "5":
        Arvore_Diretorios()
        
    elif escolha == "6":
        Estatisticas()
        
    elif escolha == "":
        print("\nObrigado por eu mesmo usar!")
        break
    
    elif escolha not in ["1", "2", "3", "4", "5", "6"]:
        print("\nPor favor, selecione uma opção valida")