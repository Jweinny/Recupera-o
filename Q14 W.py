A = int(input("Digite um numero de 1 a 5 "))

if A in range(1, 6):

    if A == 1 :
            print("Um")
    elif A == 2:
            print("dois")
    elif A == 3:
            print("Três")
    elif A == 4:
            print("quatro")
    elif A == 5:
            print("cinco")
else:
    print("Esse numero não é valido")