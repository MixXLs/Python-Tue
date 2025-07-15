max = 5
total = 0.0
print('This progam calculate the sum of')
print(max, 'numbers you will enter.')

for counter in range(max):
    number = int(input('Enter a number: '))
    total = total +number

print('The total is', total)