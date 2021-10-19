import random
def passGen():
    txt = ''
    lengh = random.randrange(7,10,1)
    for i in range(0, lengh, 1):
        txt += chr(random.randrange(33,126,1))
    return txt

print(passGen())