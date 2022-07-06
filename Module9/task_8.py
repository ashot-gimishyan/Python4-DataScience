print('Задача 8. Колонтитул')


length = int(input())
voskl = int(input())


half = (length - voskl) // 2
s = half * '~' + voskl * '!' + half * '~'

print(s)
