import random

symb = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'
number = int(input('Please, enter the number of symbols in ur password: '))

for i in range (number):
  print (random.choice(symb), end='')