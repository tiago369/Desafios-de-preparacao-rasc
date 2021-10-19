def isInteger(txt):
    txt = txt.strip()
    if(len(txt) < 1 ): return False
    elif(txt[0] == "+" and txt[1:].isnumeric()): return True
    elif(txt[0] == "-" and txt[1:].isnumeric()): return True
    elif(txt.isnumeric()): return True
    else: return False

s = str(input('Write a string to discover if is a integer: '))

if(isInteger(s) == 1): print('Is integer')
else: print('Is not integer')

