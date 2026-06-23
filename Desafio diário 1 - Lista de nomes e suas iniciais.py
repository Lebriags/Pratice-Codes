nome = ("Marcos Silva Pires, paulo  Luiz Alberto, robErto Coelho Franco ,Laisla Laisla Laisla, Pedro Joaquim Joaquim , Joaquim fernando  , luiz   ")

Resultado = []
Composto = ""
Vista = []

for i in nome.split(","):  
    
    Resultado.append(i.strip()[0])
    
    for j in i.split():
        
        if j not in Vista:
            Vista.append(j.strip())
            
            Composto = Composto + j[0].upper()
            
                
    print(Composto + str(len(Vista)))
    Composto = ""
    Vista = []