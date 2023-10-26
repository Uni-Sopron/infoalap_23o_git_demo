import math
min = math.inf

list = [1, 3, 10, 5, 20, 7, -3, -1, 'banana', 10, 100]
temp_smallest = min

for item in list:
  if item < temp_smallest:
    temp_smallest = item

print('Minimum', temp_smallest)
