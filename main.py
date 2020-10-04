from addition import *
from substraction import *
from multiplication import *
from  division import *

print('---------- This is calculator program ----------')
print('\n')

print('Please input 2 numbers')
x = float(input('1st numbers : '))
y = float(input('2nd numbers : '))

print('\n')
print('Addition result: ', add(x, y))
print('Substraction result: ', minus(x, y))
print('Multiplication result: ', multiply(x, y))
print('Division result: ', divide(x, y))
