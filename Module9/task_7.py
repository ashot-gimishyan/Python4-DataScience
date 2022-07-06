print('Задача 7. Великий и могучий')

words = input().split(' ')

max_len = 0
for word in words:
  if len(word) > max_len:
    max_len = len(word)

print('Длина самого длинного слова:', max_len)
