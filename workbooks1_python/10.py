def reductFrac(numerator, denominator):
    if(denominator >= numerator): x = denominator
    else: x = numerator

    for i in range(x,1,-1):
        if(numerator % i == 0 and denominator % i == 0):
            numerator = numerator/i
            denominator = denominator/i
    
    return [int(numerator), int(denominator)]

n = int(input('Put the numerator: '))
d = int(input('Put the denominator: '))

[x,y] = reductFrac(n,d)

print(f'{x}/{y}')
