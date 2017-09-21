a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

lst = []
for i in range(a, b+1):
    if i % 5 == 0:
        lst.append(i)
print (lst)