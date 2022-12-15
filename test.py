import random


a = [1, 2, 3, 4, 1, 4, 34, 12 , 3, 4, 4, 2, 45,2, 3, 4, 1]

for i in a:
    for j in range(1, len(a)):
        print(random.randint(3, 4))
        if a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]

print(a)


b = [2, 3, 2, 3, 2, 3, 2, 2]

c = list(map(lambda x, y: x*y, a, b))
print(c)