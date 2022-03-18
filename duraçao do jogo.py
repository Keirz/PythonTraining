data = input().split()
iniciu, finao = data

iniciu = int(data[0])
finao = int(data[1])

if iniciu < finao:
    t = finao - iniciu
else:
    t = (24 - iniciu) + finao
print('O JOGO DUROU {} HORA(S)'.format(t))
