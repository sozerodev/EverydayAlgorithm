fiboSum = 2

fibo_1 = 1
fibo_2 = 2
fibo_3 = 0

while(True):
    if(fibo_3 > 4000000):
        break

    fibo_3 = fibo_1 + fibo_2
    print("fibo_3", fibo_3)

    if(fibo_3 % 2 == 0):
        fiboSum += fibo_3

    fibo_1 = fibo_2
    fibo_2 = fibo_3


print("fiboSum", fiboSum)
