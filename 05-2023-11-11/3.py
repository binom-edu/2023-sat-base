# Даны два числа. Определить, какое из них больше
a = int(input())
b = int(input())
# вложенное ветвление
if a > b:
    print('Первое больше')
else:
    if a == b:
        print('Числа равны')
    else:
        print('Второе больше')