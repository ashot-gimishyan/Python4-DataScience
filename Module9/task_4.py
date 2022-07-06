print('Задача 4. Театр')



r = int(input('Введите кол-во рядов: '))
s = int(input('Введите кол-во сидений ряду: '))
m = int(input('Введите кол-во метров между рядами: '))

sample = '=' * s + ' ' + '*' * m + ' ' + '=' * s

for i in range(r):
  print(sample)
