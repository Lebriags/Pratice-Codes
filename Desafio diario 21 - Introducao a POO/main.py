from tkinter import filedialog
import subprocess
    
dados = []

class Programa():
    
    def __init__(self, nome, caminho, versao, estado, subprocesso):
        self.nome = nome
        self.caminho = caminho
        self.versao = versao
        self.estado = estado
        self.subprocesso = subprocesso
    
    def abrir(self):
        if self.estado == "aberto":
            print(f"{self.nome} ja esta aberto.")
            return
        try:        
            self.subprocesso = subprocess.Popen(self.caminho)
        except FileNotFoundError:
            print("Não foi possivel encontrar o programa.")
        except OSError:
            print("Não foi possivel iniciar o programa.")
        else:        
            self.estado = "aberto"
        
    def fechar(self):
        if self.estado == "fechado":
            print(f"{self.nome} ja esta fechado.")
            return
                    
        self.processo.terminate()
        self.subprocesso = None
        self.estado = "fechado"
    
def selecionar_diretorio():
    print("Procure o executavel do programa: ")
    caminho = filedialog.askopenfilename()
    
    if not caminho:
        print("Nenhum arquivo selecionado.")
        return None
    
    return caminho
    
def limpar(): 
    import os 
    os.system('cls' if os.name == 'nt' else 'clear')

def cadastrar_programa():
    
    limpar()
        
    print("Cadastrar um programa:\n")
        
    nome = input("Digite o nome do programa: ")
    caminho = selecionar_diretorio()
    if caminho is None: 
        print("Cadastro cancelado.")
        return
    versao = input("Informe a versão do programa: ")
    estado = "fechado"
    subprocesso = None
        
    programa = Programa(
        nome,
        caminho,
        versao,
        estado,
        subprocesso
    )
        
    dados.append(programa)
    print(f"\n{programa.nome} Registrado!")
        
    input("\nPressione ENTER para retornar...")

def listar_programas():
    
    limpar()
        
    if dados == []:
        print("Não há programas cadastrados.")
    else:
        print("Todos os programas cadastrados: \n")
        
        for programa in dados:
            print(programa.nome)
        
    input("\nPressione ENTER para voltar...")

def abrir_programa(): 
    
    limpar()
        
    print("Abrir um programa: \n")
        
    if dados == []:
        print("Não há programas cadastrados.")
    else:
        for indice, programa in enumerate(dados):
            print(f"{indice} - {programa.nome}")
        
    try:    
        escolha = int(input("\nDigite o numero do programa que deseja abrir: "))
    except ValueError:
        print("Digite apenas numeros")
        return
        
    indice = escolha - 1
    programa = dados[indice]
    programa.abrir()
        
    input("\nPressione ENTER para retornar ao menu...")

def fechar_programa():
    
    limpar()
        
    print("Fechar um programa: \n")
        
    if dados == []:
        print("Não há programas cadastrados.")
    else: 
        for indice, programa in enumerate(dados):
            print(f"{indice} - {programa.nome}")
        
    try:            
        escolha = int(input("\nDigite o numero do programa que deseja abrir: "))
    except ValueError:
        print("Digite apenas numeros")
        return

    if escolha < 1 or escolha > len(dados):
        print("Programa invalido")
        return
                        
    indice = escolha - 1
    programa = dados[indice]
    programa.fechar()
                
    input("\nPressione ENTER para retornar ao menu...")

def consultar_estado_programa():
    
    limpar()
        
    print("Estado atual de programas cadastrados: \n")
        
    if dados == []:
        print("Não há programas cadastrados.")
    else:
        for programa in dados:
            print(f"{programa.nome} - Estado: {programa.estado}")
            
    input("\nDigite enter para retornar ao menu...")

def menu():
    
    while True:
        limpar()
        
        print("Programas instalados no computador.\n")
        
        print("[1] - Cadastrar um programa.")
        print("[2] - Listrar programas cadastrados.")
        print("[3] - Abrir um programa.")
        print("[4] - Fechar um programa.")
        print("[5] - Consutar estado de um programa.\n")
        
        escolha = input("Digite a opção desejada (Ou ENTER para fechar): ")
        
        if escolha == "1":
            cadastrar_programa()
            
        elif escolha == "2":
            listar_programas()

        elif escolha == "3":
            abrir_programa()
        
        elif escolha == "4":
            fechar_programa()
        
        elif escolha == "5":
            consultar_estado_programa()
        
        elif escolha == "":
            print("Obrigado por testar.")
            print("\nFechando...")
            return
        
        elif escolha not in ["1" , "2" , "3" , "4" , "5"]:
            print("Por favor, selecione uma opção valida")

menu()