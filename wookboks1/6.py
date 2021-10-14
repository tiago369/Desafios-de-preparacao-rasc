def isPrime(n):
    count=0
    if(n == 1): return True
    for i in range(2, n, 1):
        if(n % i == 0): count += 1
    if(count > 1): return False
    else: return True

num = int(input('Digite o numero que voce deseja descobrir se é primo: '))

if(isPrime(num)): print('É primo')
else: print('Não é primo')
