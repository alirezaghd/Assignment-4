import math

#  a * x **3 + b * x ** 2 + c * x + d = 0

def delta(a,b,c,d):
    p = ((18 * a) * b * c * d) - ((4 * b) ** 3 * d)  + (b ** 2) * (c ** 2) - (4 * a) * (c ** 4) - (27* (a **2)) * (d ** 2)
    return p


a = int(input())
b = int(input())
c = int(input())
d = int(input())

w = delta(a,b,c,d)

if w > 0 :
   x = (2 * b) ** 3 - 9 * a * b *c + 27 * a ** 2 * d
   print(x)

elif w == 0 :
    x1 =  b ** 2 - 3 * a * c

elif w < 0 :
    print("be moshkel khordam :)")