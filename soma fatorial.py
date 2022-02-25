# -*- coding: utf-8 -*-
try:
  while True:
    txt = input().split(' ')
    M = int(txt[0])
    N = int(txt[1])
    result1 = N
    result = M
    if M == 0:
      result = 1
    if N == 0:
      result1 = 1
  
    for i in range(1,M):
      result = result * i
    for i in range(1,N):
      result1 = result1 *i
    print(result1+result)
except:
  pass
