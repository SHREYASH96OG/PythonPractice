num = 15
flag = 0
if num<2:
  flag = 1
else:
  for i in range(2,num):
    if num%i==0:
      flag = 1
      break

if flag == 1:
  print('Not Prime')
else:
  print("Prime")