import random
cor=int()
incor=int()
for i in range(1,100):
    a=random.randint(1,9)
    b=random.randint(1,9)
    print("решите уравнение: ", a," X ", b)
    print("правильно: " ,cor ," не правильно: ", incor)
    c=int(input())
    if c == (a*b):
        cor=cor+1
    else:
        incor=incor+1
    i=i+1
