a = float(input())
if 0<= a <= 25:
    print('Intervalo [0,25]')
if 25< a <= 50:
    print('Intervalo (25,50]')
if 50< a <= 75:
    print('Intervalo (50,75]')
if 75< a <= 100:
    print('Intervalo (75,100]')
if a >100 or a<0:
    print('Fora de intervalo')
