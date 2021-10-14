import decimal

def magicDate(day, mounth, year):
    y = int((decimal(year/100) - int(year/100))*100)
    if(day * mounth == y):
        return True
    else: return False

def printMD(aday, amounth, ayear):
    if(magicDate(aday, amounth, ayear)):
        print(f'Day {aday}, from mounth {amounth} of {ayear} is a magic date')


for y in range(1901, 2001, 1):
    for m in range(1, 13, 1):
        if(m % 2 != 0):
            for dj in range(1, 32, 1):
                printMD(dj, m, y)
        elif(m % 2 == 0 and m != 2):
            for da in range(1, 31, 1):
                printMD(da,m,y)
        else:
            if(y % 4 == 0):
                for dfb in range(1, 30, 1):
                    printMD(dfb,m,y)
            if(y % 4 != 0):
                for df in range( 1, 29, 1):
                    printMD(df,m,y)
            