# возвести все четные элементы списка в квадрат
import random
a = [random.randint(-10, 10) for i in range(5)]
print(a)

for i in a:
    if i % 2 == 0:
        i = i ** 2

print(a)
# список не изменился!

for i in range(len(a)):
    if a[i] % 2 == 0:
        a[i] = a[i] ** 2
print(a)
# список изменился!