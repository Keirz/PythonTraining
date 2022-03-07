from math import sqrt
while True:
    try:
        d, vf, vg = [int(a) for a in input().split()]
        vg = (sqrt(144 + (d * d)))/vg
        vf = 12/vf
        if vg > vf:
            print('N')
        else:
            print('S')
    except EOFError:
        break
