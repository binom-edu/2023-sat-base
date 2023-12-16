# посчитать сумму чисел от 1 до n включительно

n = int(input())
ans = 0
for i in range(1, n + 1):
    ans += i
print(ans)