# -*- coding: utf-8 -*-

predio = [int(input()) for andar in range(3)]
tempo_total = []
tempo_total.append(predio[0]*4 + predio[1]*2)
tempo_total.append(predio[0]*2 + predio[2]*2)
tempo_total.append(predio[1]*2 + predio[2]*4)

tempo_total.sort()
print(tempo_total[0])
