def toBase10(num, orig_base):
    base = 0
    if(num == 10): return orig_base
    elif(num >= 2 and num <= 16):
        for i in range(0, len(orig_base), 1):
            if(orig_base[i] == 'A' or orig_base[i] == 'a'):
                base += 10 * (num ** i)
            elif(orig_base[i] == 'B' or orig_base[i] == 'b'):
                base += 11 * (num ** i)
            elif(orig_base[i] == 'C' or orig_base[i] == 'c'):
                base += 12 * (num ** i)
            elif(orig_base[i] == 'D' or orig_base[i] == 'd'):
                base += 13 * (num ** i)
            elif(orig_base[i] == 'E' or orig_base[i] == 'e'):
                base += 14 * (num ** i)
            elif(orig_base[i] == 'F' or orig_base[i] == 'f'):
                base += 15 * (num ** i)
            else:
                base += orig_base[i] * (num ** i)
    else:
        return 'ERROR'
    return str(base)

def decToBaseX(num, orig_base):
    txt = ''
    txt2 = ''
    if(num == 10): return orig_base
    elif(num >= 2 and num <= 9):
        obase = int(orig_base)
        for i in range(0, len(obase), 1):
            rest = obase % num
            obase = obase // num
            txt += str(rest)
        for j in range(len(obase), 0, -1):
            txt2 += txt[j]

def yToBaseX(o_base, f_base, txt):
    return decToBaseX(f_base, toBase10(o_base, txt))