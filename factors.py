import math
str_num = input('What number do you want the factors of?: ')
num = int(str_num)
factors = []

for i in range(2, num):
    if num%i == 0:
        factors.append(i)
print('The factors are: ' + str(factors))
