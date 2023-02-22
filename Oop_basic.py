class bio:

    # class attribute
    name = ""
    age = 0

# create parrot1 object
bio1 = bio()
bio2 = bio()
#assigning values to attributes of obj
bio1.name = "Shreyash"
bio2.name = "Golu"
bio1.age = 22
bio2.age = 18

# access attributes
print(f"my name is {bio1.name} and  age is {bio1.age}")


"""
O/P
my name is Shreyash and age is 22
"""
