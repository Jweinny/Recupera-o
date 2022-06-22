N = int(input("Ler N numeros: "))

for i in range(0, N):
    A =int(input("Digite um numero: "))
    
    if  A == 0 :
        print("Ele é igual a 0")
    elif A > 0:
        print("Ele é positivo")
    elif A < 0:
        print("Ele é negativo")

