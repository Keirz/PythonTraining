import math
def e_primo(n):
    if n%2 == 0 and n>2:
        return False
    return all(n%i for i in range(3,int(math.sqrt(n))+1, 2))
T = int(input())
for _ in range(T):
    a = int(input())
    if (e_primo(a)):
        print('Prime')
    else:
        print('Not Prime')
