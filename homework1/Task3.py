n = int(input("Введите число n = "))
lst = []
for i in range(2, n+1):
    for j in lst:
        if i % j == 0:
            break
    else:
        lst.append(i)
print (lst)