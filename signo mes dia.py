print('Digita o mês e dia do nascimento, na respectiva ordem e sem sinais:')


dados = list(map(int, input().split()))

mes, dia = dados


if mes == 12 and 22 <= dia <= 31 or mes == 1 and 1 <= dia <= 20:

    print('capricornio')


elif mes == 1 and 21 <= dia <= 31 or mes == 2 and 1 <= dia <= 18:

    print('aquario')



elif mes == 2 and 19 <= dia <= 29 or mes == 3 and 1 <= dia <= 19:

    print('peixes')



elif mes == 3 and 20 <= dia <= 31 or mes == 4 and 1 <= dia <= 20:

    print('aries')


elif mes == 4 and 21 <= dia <= 30 or mes == 5 and 1 <= dia <= 20:

    print('touro')



elif mes == 5 and 21 <= dia <= 31 or mes == 6 and 1 <= dia <= 20:

    print('gemeos')

elif mes == 6 and 21 <= dia <= 30 or mes == 7 and 1 <= dia <= 21:

    print('cancer')

elif mes == 7 and 22 <= dia <= 31 or mes == 8 and 1 <= dia <= 22:

    print('leao')

elif mes == 8 and 23 <= dia <= 31 or mes == 9 and 1 <= dia <= 22:

    print('virgem')

elif mes == 9 and 23 <= dia <= 30 or mes == 10 and 1 <= dia <= 22:

    print('libra')

elif mes == 10 and 23 <= dia <= 31 or mes == 11 and 1 <= dia <= 21:

    print('escorpiao')

elif mes == 11 and 22 <= dia <= 30 or mes == 12 and 1 <= dia <= 21:

    print('sagitario')



else:

    print('mes ou dia invalido')
