
x = 8
y = 10

print("Марсоход находится на позиции " + str(x) + ', ' + str(y) + ". Ведите команду:")
inp = input('[Оператор]: ')

while inp not in ['A', 'W', 'S','D']:
  inp = input('[Оператор]: ')

while inp in ['A', 'W', 'S','D']:
  if 0 < x < 15:
    if inp == 'A':
      x -= 1
    if inp == 'D':
      x += 1

  if 0 < y < 20:
    if inp == 'W':
      y += 1
    if inp == 'S':
      y -= 1

  if x == 0 and inp == 'D':
    x+=1

  if y == 0 and inp == 'W':
    y+=1

  if x == 15 and inp == 'A':
    x-=1

  if y == 20 and inp == 'S':
    y-=1

  print("Марсоход находится на позиции " + str(x) + ', ' + str(y) + ". Ведите команду:")
  inp = input('[Оператор]: ')

