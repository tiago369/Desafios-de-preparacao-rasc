from typing import Text


def center_string (text, spaces):
    c =''
    a = len(text)
    b = (spaces/2) - (a/2) 
    for i in range(0, int(b), 1):
        c += ' '
    c += text
    return c


t = str(input('texto: '))
s = int(input('espaços: '))

print(center_string(t,s))