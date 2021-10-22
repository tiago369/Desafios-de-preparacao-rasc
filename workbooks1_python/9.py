def toBase10(num, orig_base):
    base = 0
    if(num == 10): return orig_base
    elif(num >= 2 and num <= 16):
        j = len(orig_base) - 1
        for i in range(0, len(orig_base), 1):
            if(orig_base[i] == 'A' or orig_base[i] == 'a'):
                base += 10 * (num ** j)
            elif(orig_base[i] == 'B' or orig_base[i] == 'b'):
                base += 11 * (num ** j)
            elif(orig_base[i] == 'C' or orig_base[i] == 'c'):
                base += 12 * (num ** j)
            elif(orig_base[i] == 'D' or orig_base[i] == 'd'):
                base += 13 * (num ** j)
            elif(orig_base[i] == 'E' or orig_base[i] == 'e'):
                base += 14 * (num ** j)
            elif(orig_base[i] == 'F' or orig_base[i] == 'f'):
                base += 15 * (num ** j)
            else:
                base += int(orig_base[i]) * (num ** j)
            j -= 1
    else:
        return 'ERROR'
    return str(base)

def decToBaseX(num, orig_base):
    txt = ''
    txt2 = ''
    if(num == 10): return orig_base
    elif(num >= 2 and num <= 16):
        obase = int(orig_base)
        while(obase >= num):
            rest = obase % num
            obase = obase // num
            if(rest == 10):
                txt += 'A'
            elif(rest == 11):
                txt += 'B'
            elif(rest == 12):
                txt += 'C'
            elif(rest == 13):
                txt += 'D'
            elif(rest == 14):
                txt += 'E'
            elif(rest == 15):
                txt += 'F'
            else:
                txt += str(rest)
        txt += str(obase)
        for j in range(len(txt)-1, -1, -1):
            txt2 += txt[j]
    return txt2

def yToBaseX(o_base, f_base, txt):
    return decToBaseX(f_base, toBase10(o_base, txt))

x = str(input('Digite a base:'))
y = int(input('Digite qual o valor da base dele: '))
z = int(input('Digite para qual base deseja converter: '))

print(yToBaseX(y,z,x))
