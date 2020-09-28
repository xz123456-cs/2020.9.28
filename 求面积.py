import math
sum_x = 0
area_z = 0
min = 0.00001
p = math.pi
while sum_x <= 2*p:
    y_z = math.sin(sum_x)
    y=abs(y_z)
    area_1 = min*y
    area_z = area_z+area_1
    sum_x = sum_x+min
print(area_z)