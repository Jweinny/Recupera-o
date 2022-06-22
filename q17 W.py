A = int(input("Digite um numero de 1 e 12 "))
mes = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'março',
    4: 'abril',
    5: 'Maio',
    6: 'Junho',
    7: 'julho',
    8: 'agosto',
    9: 'setembro',
    10: 'outubro',
    11: 'novembro',
    12: 'Dezembro',
    
    
}


if A in range(1, 13):
    print(mes.get(A))
else:
    print("Esse numero não é valido")