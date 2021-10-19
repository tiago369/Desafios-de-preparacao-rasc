def palindrome(txt):
    txt = txt.lower()
    txt2 = ''
    for i in range(len(txt)-1, -1, -1):
        txt2 += txt[i]
    if(txt == txt2): return True
    else: return False

p = str(input('Put a message to discorver if is a palindrome or not: '))
if(palindrome(p)):
    print('The message is a palindrome')
else:
    print('The message its not a palindrome')
