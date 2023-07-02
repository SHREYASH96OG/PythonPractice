#first we specify size of list
l = int(input("enter the length of list"))
li = []
for i in range(l):
    #here we add element in list
    el = int(input("enter element"))
    li.append(el)
#code is for sorting a list
n = []
while li:
    mi = li[0]
    for x in li:
        if x < mi:
            mi = x
    n.append(mi)
    li.remove(mi)
print(n)