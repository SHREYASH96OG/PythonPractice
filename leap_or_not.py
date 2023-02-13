y = int(input("Enter the year :"))
if((y%4==0 or y%100 == 0)and y%400!= 0):
    print("Not leap a year")
else:
    print("leap year")