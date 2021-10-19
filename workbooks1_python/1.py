def median(a, b, c):
    if(c >= a >= b or b >= a >= c):
        return a
    elif(c >= b >= a or a >= b >= c):
        return b
    else:
        return c

print('Digite 3 valores para tirar sua mediana')
x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))

print(f'Esses valores tem como mediana {median(x,y,z)}')