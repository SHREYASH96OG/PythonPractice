num = int(input("Enter the number:"))

for i in range(num):
    for j in range(1, i+1):
        print(" ", end="")
    for j in range(0, num):
        print("*", end="")
    print()
