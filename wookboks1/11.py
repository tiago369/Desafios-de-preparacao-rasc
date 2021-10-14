def converter(number, unit):
    if(unit != 'cup' and unit != 'tablespoon' and unit != 'teaspoon'): return 'Invalid unit'
    
    if(unit == 'tablespoon'):
        cv = number * 3
    if(unit == 'teaspoon'):
        cv = number
    elif(unit == 'cup'):
        return number + 'cup'

    cup = int(cv/48)
    cv = cv % 48
    tbsp = int(cv/3)
    cv = cv % 3
    teasp = cv

    return str(cup) + ' cup ' + str(tbsp) + ' tablespoon ' + str(teasp) + ' teaspoon'

n = int(input('N: '))
d = str(input('D: '))

print(converter(n,d))