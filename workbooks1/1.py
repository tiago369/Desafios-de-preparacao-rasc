def median(a, b, c):
    if(a > b and a > c):
        return a
    elif(b > a and b > c):
        return b
    else:
        return c

print('Digite 3 valores para tirar sua mediana')
x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))

print(f'Tem como mediana {median(x,y,z)}')