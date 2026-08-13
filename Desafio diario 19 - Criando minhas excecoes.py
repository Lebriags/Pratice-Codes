# Mini Laboratório de Execões, tratanto todas as tasks que a atividade pede.

''' 
    - Erro de Nome
    - Erro de Idade
    - Erro de Comando
'''
class AlfredoError(Exception):
    pass

class NomeInvalidoError(AlfredoError):
    pass

class IdadeInvalidaError(AlfredoError):
    pass

class ComandoInvalidoError(AlfredoError):
    pass


dados = {"Nome" : "Anderson", "Idade" : 0, "Comando" : "Fechar_Aba"}

def ExemploExecaoPronta():
    
    try:
        nome = input("Digite um nome de usuário")
        if dados["Nome"] != nome:
            raise NomeInvalidoError()
        
        idade = int(input("Digite uma idade"))
        if dados["Idade"] != idade:
            raise IdadeInvalidaError()
        
        comando = input("Digite um comando")
        if dados["Comando"] != comando:
            raise ComandoInvalidoError()
        
    except NomeInvalidoError:
        print("O nome que você digitou não é o correto")
    
    except IdadeInvalidaError:
        print("A idade esta errada")
        
    except ValueError:
        print("Digite um numero")
        
    except ComandoInvalidoError:
        print("O comando esta incorreto")
        
    else:
        print("Tudo certo, todos os campos verificados corretamente!")
        
    finally:
        print("Voltando...")

def ExemploExecaoCriada():
    pass

while True:
    
    print("[1] - Testar Exeções com valores ja definidos.")
    print("[2] - Adicionar Valores e testar as Exeções")
    print("Pressione ENTER para sair...")
    
    escolha = input("Digite sua escolha: ")
    
    if escolha == "1":
        ExemploExecaoPronta()
        
    elif escolha == "2":
        ExemploExecaoCriada()
    
    elif escolha == "":
        break