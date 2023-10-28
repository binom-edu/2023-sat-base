a = int(input())
b = int(input())
n = int(input())
p = a * 100 + b # цена пирожка в копейках
total = p * n # стоимость покупки в копейках
print(total // 100, total % 100) # получаем обратно рубли и копейки