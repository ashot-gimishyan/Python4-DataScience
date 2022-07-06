print('Задача 3. Кривой мессенджер')


text = input("Введите текст: ")

for i in range(len(text)):
  if text[i] == '*':
    print('Символ ‘*’ стоит на позиции', i+1)
    break
  
