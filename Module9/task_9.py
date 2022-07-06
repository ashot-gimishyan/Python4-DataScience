print('Задача 9. Коровы')

total_milk = 0
ab_string = input()

for i in range(len(ab_string)):
  if ab_string[i] == 'a':
    continue

  if ab_string[i] == 'b':
    total_milk += (2 * (i+1))


print(total_milk)
    
