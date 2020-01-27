print('{:_<10}'.format('test'))
print('{} {}'.format(1, 2))
print('{:10.5}'.format('xylophone'))
print('{:06.2f}'.format(3.141592653589793))

data = {'first': 'Hodor', 'last': 'Hodor!'}
print('{first} {last}'.format(**data))