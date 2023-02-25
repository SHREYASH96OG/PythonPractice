arr = [10, 89, 9, 56, 4, 80, 8]
mini = arr[0]

for i in range(len(arr)):
  if arr[i] < mini:
     mini = arr[i]

print (mini)
