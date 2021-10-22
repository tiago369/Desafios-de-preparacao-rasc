def music(verse):
    if(verse > 102): return ''
    pos = 3
    count = 0
    n = verse
    days = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh','twelfth']
    vs3 = ['A partridge in a pear tree.','And partridge in a pear tree.']
    vs2 = ['Twelve fiddlers fiddling,','Eleven ladies dancing,','Ten pipers piping,','Nine drummers drumming,','Eight maids a-milking,','Seven swans a-swimming,','Six geese a-laying,','Five gold rings,','Four colly birds,','Three French hens,','Two turtle doves']
    
    vs1 = ['Two turtle doves','Three French hens,','Four colly birds,','Five gold rings,','Six geese a-laying,','Seven swans a-swimming,','Eight maids a-milking,','Nine drummers drumming,','Ten pipers piping,','Eleven ladies dancing,','Twelve fiddlers fiddling,']
    
    while(n >= pos):
            n = n - pos
            pos += 1
    estrofe = pos - 3
    print(n)
    print(pos)
    print(estrofe)

    if(n == 1):
        return 'The '+ days[estrofe-1] + ' day of Christmas,'
    elif(n == 2):
        return 'My true love sent to me'
    elif(n == 0 and estrofe == 1):
        return vs3[0]
    elif(n == 0 and estrofe != 1):
        return vs3[1]
    else:
        x = vs2[11-estrofe + n-3]
        return x


v = int(input('Digite o verso que deseja achar: '))

print(music(v))
