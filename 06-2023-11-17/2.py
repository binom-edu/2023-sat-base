# дано число. Определить, является ли оно простым
n = int(input())
d = 2
while d < n:
    if n % d == 0:
        print('NO')
        break
    d += 1
else:
    print('YES')