#-*- coding: utf-8 -*-

while 1:
    qnt = int(input())
    if (qnt == 0):
        break
    resultados = list(map(int,input().split()))
    a = 0
    b = 0
    for c in resultados:
        if(c == 0):
            a += 1
        else:
            b += 1
    print("Mary won %d times and John won %d times"%(a,b))
