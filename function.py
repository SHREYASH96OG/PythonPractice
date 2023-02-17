# simple function implemented to check whether number is even or odd which 

def even_odd(n):
    if n%2==0:
        print(n,"is Even")
    else:
        print(n,"is Odd")
    

n = int(input("enter the numbere to check that it is even or odd :"))
even_odd(n)
