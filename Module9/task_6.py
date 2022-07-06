print('Задача 6. Спецшифр')


string = input('Введите строку: ')

count = 0
maxx_s = count

for sym in string:
  if sym == 's':
    count += 1
    continue

  if count > maxx_s:
    maxx_s = count
    
  count = 0

print('Самая длинная последовательность:', maxx_s)
