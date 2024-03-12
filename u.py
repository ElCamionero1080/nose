import random
n = input("ingresa un nombre -> ")
m = input("ingresa un nombre -> ")
a=0
b=0
while a<5 or b<5:
    c = random.randint(1,2)
    if c==1:
        a+=1
        print(n)
    else:
        b+=1
        print(m)
    if a==5:
            print("Gano",n)
            print(a,"-",b)
            break
    elif b==5:
            print("Gano",m)
            print(a,"-",b)
            break
