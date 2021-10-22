def perfect_num(num):
    cont = 0
    for i in range(1, num, 1): 
        if(num % i == 0):
            cont += i
    if(cont == num):
        return True
    else:
        return False

print('Perfect numbers:')
for i in range(1, 10000, 1):
    if(perfect_num(i)):
        print(i)
