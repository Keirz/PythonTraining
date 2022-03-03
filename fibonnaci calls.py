fibo = [1, 1]
qt = [0, 1]
for i in range(2, 41):
    fibo.append(fibo[i-1] + fibo[i-2] + 1)
    qt.append(qt[i-1] + qt[i-2])
    
t = int(input())
while(t > 0):
    n = int(input())
    print("fib(%d) = %d calls = %d" %(n, fibo[n]-1, qt[n]))
    t -= 1
