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

    if(cup > 1):
        c = ' cups, '
    else:
        c = ' cup, '
    if(tbsp > 1):
        t = ' tablespoons, '
    else:
        t = ' tablespoon, '
    if(teasp > 1):
        te = ' teaspoons'
    else:
        te = ' teaspoon'

    return str(cup) + c + str(tbsp) + t + str(teasp) + te

n = int(input('Put the unit quantity: '))
d = str(input('Put the unit name (cup/tablespoon/teaspoon): '))

print(converter(n,d))