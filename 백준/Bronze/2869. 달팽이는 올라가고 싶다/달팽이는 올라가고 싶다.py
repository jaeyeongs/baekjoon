import math
# A = 올라가는 길이, B = 떨어지는길이, V = 나무높이 
A, B, V = map(int, input().split())
day = math.ceil((V-A)/(A-B)) + 1
print(day)