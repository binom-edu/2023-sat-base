# минимальная цифра числа
n = int(input())
ans = 9
while n > 0:
    d = n % 10
    # что-то делаем с последней цифрой
    if d < ans:
        ans = d
    # остальное не меняется
    n = n // 10

print(ans)