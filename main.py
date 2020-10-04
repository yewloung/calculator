from addition import *
from substraction import *
from multiplication import *
from division import *

print('---------- This is calculator program ----------')
print('\n')

print('Please input 2 numbers')
x = float(input('your 1st numbers : '))
y = float(input('your 2nd numbers : '))

print('\n')
print('Calculation result:')
print(x, '+', y, '=', add(x, y))
print(x, '-', y, '=', minus(x, y))
print(x, '*', y, '=', multiply(x, y))
print(x, '/', y, '=', divide(x, y))
