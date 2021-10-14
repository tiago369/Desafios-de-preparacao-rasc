def music(verse):
    if(verse > 102): return ''
    pos = 3
    count = 0
    n = verse
    days = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh','twelfth']
    vs1 = ['A partridge in a pear tree.','And partridge in a pear tree.','Two turtle doves','Two turtle doves','Three French hens,','Four colly birds,','Five gold rings,','Six geese a-laying,','Seven swans a-swimming,','Eight maids a-milking,','Nine drummers drumming,','Ten pipers piping,','Eleven ladies dancing,','Twelve fiddlers fiddling,']
    while(n > pos):
            n = n - pos
            pos += 1
    estrofe = pos - 2
    print(pos)
    print(estrofe)

    if(pos == 1):
        return 'The '+ days(estrofe-1) + ' day of Christmas,'
    elif(pos == 2):
        return 'My true love sent to me'
    elif(pos == 0 and estrofe == 1):
        return days[11]
    elif(pos == 0 and estrofe != 1):
        return vs1[0]
    else:
        for i in range(estrofe, 1, -1):
            x = vs1[i]
        return x


v = int(input('->'))

print(music(v))
