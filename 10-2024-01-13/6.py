# итерация по списку
import random
a = [random.randint(-10, 10) for i in range(5)]
print(a)

for i in range(len(a)):
    print(a[i])

print('---')

for element in a:
    print(element)
    # изменять элементы списка не получится!