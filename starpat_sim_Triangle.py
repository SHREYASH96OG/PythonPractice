num = int(input("Enter the Number: "))

for i in range(0, num):
    for j in range(0, num-i-1):
        print(" ", end="")
    for j in range(0, i*2+1):
        print("*", end="")
    print()