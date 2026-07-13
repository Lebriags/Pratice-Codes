# notas = []   
    
while True:
    
    receber = input("Digite as notas em ordem separados por virgula: ").split(",")
    # notas.extend(receber)
    
    soma_tudo = 0
    
    total = len(receber)
    
    maior = receber[0]
    menor = receber[0]
    acima_da_media = 0

    for nota in receber:
        
        soma_tudo += int(nota)
    
        if int(nota) > int(maior):
            maior = nota
        elif int(nota) < int(menor):
            menor = nota
          
    media = float(soma_tudo / total)
    
    for nota in receber:
        if int(nota) > float(media):
            acima_da_media += 1 
    
    print(f"Quantidade: {total}\nMédia: {media}\nMaior: {maior}\nMenor: {menor}\nAcima da Média: {acima_da_media}")
    sair = input("Para sair, digite 'fim': ")
    
    if sair == "fim".lower():
        print("Volte sempre!")
        exit()
