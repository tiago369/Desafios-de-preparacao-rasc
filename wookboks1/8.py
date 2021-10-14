def passCheck(password):
    ucase = 0
    lcase = 0
    num = 0
    if(len(password) < 8): return False
    for i in range(0,len(password)-1,1):
        if(password[i].isupper()): ucase += 1
        elif(password[i].islower()): lcase += 1
        elif(password[i].isnumeric()): num += 1
    if(ucase >= 1 and lcase >= 1 and num >= 1): return True
    else: return False

p = str(input('->'))

print(passCheck(p))

