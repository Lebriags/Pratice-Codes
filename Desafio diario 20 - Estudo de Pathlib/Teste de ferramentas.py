'''
    Exceções do pathlb
    
    - FileNotFoundError
    - FileExistsError
    - PermissionError
    - OSError
    
'''


from pathlib import Path

'''resposta = Path.cwd()
resposta2 = Path.home()
resposta3 = Path("F:\\Coding\\Projeto medio\\bibliotecapy\\main.py").is_file()
resposta4 = Path("F:\\Coding\\Projeto medio\\bibliotecapy").is_file()
resposta5 = Path("F:").is_dir()
resposta6 = Path("F:\\Coding\\Projeto medio\\bibliotecapy\\main.py").name
resposta7 = Path("F:\\Coding\\Projeto medio\\bibliotecapy\\main.py").suffix
resposta8 = Path("F:\\Coding\\Projeto medio\\bibliotecapy\\main.py").stem
resposta9 = Path("F:\\Coding\\Projeto medio\\bibliotecapy\\main.py").parent

resposta10 = Path("F:\\Coding\\Desafio Diário").iterdir()


    
resposta12 = Path("C:\\Users\\CC3\\Downloads")
for caminho in resposta12.glob("*.jpg"):
    print(caminho)

resposta13 = Path("F:\\Coding\\Projeto medio\\bibliotecapy\\main.py").stat().st_size'''

'''try:
    resposta14 = Path("Desafio diario 20 - Estudo de Pathlib\\mkdirteste")
    resposta14.mkdir()
except FileExistsError:
    print("ln 38: Pasta ja existe")
    
try:
    resposta15 = Path("Desafio diario 20 - Estudo de Pathlib\\mkdirteste\\Jay\\May\\January")
    resposta15.mkdir(parents=True) 
except FileExistsError:
    print("ln 44: Cadeia de arquivos ja criada")
    
#Versão que não precisa de except:
resposta16 = Path("Desafio diario 20 - Estudo de Pathlib\\mkdirteste\\Jay\\May\\January")
resposta15.mkdir(parents=True, exist_ok=True)   
    
print(resposta)
print(resposta2)
print(resposta3)
print(resposta4)
print(resposta5)
print(resposta6)
print(resposta7)
print(resposta8)
print(resposta9)

print("")

print(resposta10)

print("")

print(resposta13)'''

resposta11 = Path("F:\\Coding\\Projeto medio\\bibliotecapy")
for a in resposta11.iterdir():
    print(a)
    
resposta14 = Path("F:\\Coding\\Projeto medio\\bibliotecapy")
for a in resposta14.iterdir():
    print(a.name)
    
