n1  = int(input())
n2 = int(input())
Hcf = 0
for i in range(1,min(n1,n2)):
    if n1%i == 0 and n2%i == 0:
        Hcf = i

print("HCF of num1",n1,n2,"is the",Hcf)            