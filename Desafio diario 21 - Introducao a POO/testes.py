# Por convenção, classes tem que ser escritas em PascalCase, ja variaveis e funções são em snake_case.

'''class Programa:

    def __init__(self, nome, caminho, versao, estado):
        self.name = nome
        self.caminho = caminho
        self.versao = versao
        self.estado = estado
        
    def abrir(self):
        if self.estado == "aberto":
            print(f"{self.name} ja esta aberto.")
            return
        
        self.estado = "aberto"
    
    def fechar(self):
        if self.estado == "fechado":
            print(f"{self.name} ja esta fechado.")
            return
        
        self.estado = "fechado"

firefox = Programa(
    "Firefox",
    "C:\\Program Files\\Firefox",
    "142.0",
    "fechado"
)

# firefox.abrir()
firefox.fechar()
print(firefox.name , firefox.caminho , firefox.versao , firefox.estado)'''