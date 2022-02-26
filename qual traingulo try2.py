# -*- coding: utf-8 -*-
data = list(map(int, input().split()))
data.sort()
A,B,C = data
if (A+B<=C):
    print("Invalido")
if (A==B and B==C):
        triang = "Valido-Equilatero"
if (B==C or A==B):
        triang = "Valido-Isoceles"
elif(A!=B and C!=B or B!=C and A!=B):
        triang = "Valido-Escaleno"
if(((A**A)+(B*B))==(C*C)):
    ret ='S'
else:
    ret = 'N'
print(triang)
print("Retangulo:",ret)
