purch = int(input('Введите кол-во заказов: '))

dct = dict()
for i in range(purch):
    print(f'{i+1} заказ: ', end="")
    x = input().split()

    if x[0] not in dct:
        dct[x[0]] = list()
    dct[x[0]].append((x[1], int(x[2])))

# сортировка списка кортежей по второму "параметру"
for value in dct.values():
    value = value.sort(key = lambda m: m[1])

for key in dct.keys():
    print(key + ":")
    for elem in dct[key]:
        print("\t" + elem[0] + ": " + str(elem[1]))

