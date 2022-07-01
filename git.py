a = int(input('number1'))
b = int(input('number1'))

f = int(input('number2'))
l = int(input('number2'))

c = a * b
g = f * l

if c < g:
    print(b)
elif g < c:
    print(a)
else:
    print('the same')
