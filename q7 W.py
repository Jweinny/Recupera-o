contagem = 0
Z=0
for i in range(0, 56):
    sexo = input("Digite seu sexo H para homem e M mulher ")
    Nome = input("Digite seu nome ")
    if sexo == "H":
        contagem += 1 
    elif sexo == "M":
        Z = Z+1
    print(Nome)
    
print("A contagem de Homens é %d" %contagem)  
print("A contagem de Mulheres é %d" %Z)  



        

        
