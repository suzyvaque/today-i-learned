a = int(input())
b = int(input())

num3 = a * (b%10)
num4 = a * ((int(b/10))%10)
num5 = a * int(b/100)
num6 = num3 + num4*10 + num5*100

print(num3, num4, num5, num6, sep="\n")