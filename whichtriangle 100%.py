# -*- coding: utf-8 -*-

data = list(map(int, input().split()))
data.sort()
ladoUm,ladoDois,ladoTres = data

if(ladoUm+ladoDois<=ladoTres or ladoTres+ladoDois<=ladoUm or ladoUm+ladoTres<=ladoDois):
    {
    print("Invalido")
    }
else:
    if(ladoUm == ladoDois and ladoDois == ladoTres and ladoUm == ladoTres):
        print("Valido-Equilatero")
    

    elif(ladoDois==ladoTres or ladoUm==ladoDois or ladoUm == ladoTres):
        print("Valido-Isoceles")

    else:
        print("Valido-Escaleno")
    if(pow(ladoUm,2)+pow(ladoDois,2))==pow(ladoTres,2):
            ret = 'S'
    else:
            ret = 'N'       
    print("Retangulo:", ret)
