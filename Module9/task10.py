print('Задача 10. Метод бутерброда')

word = input()

'''
dec = ""
for i in range(len(word)//2):
  dec += word[i]
  dec += word[len(word) - i - 1]

if len(word) % 2 == 1:
  dec += word[len(word)//2]

print(dec)
'''


enc = ""
for i in range(0, len(word), 2):
  enc += word[i]

for i in range(len(word)- 1 - int(len(word) % 2 == 1), -1, -2):
  enc += word[i]
  

print(enc)


