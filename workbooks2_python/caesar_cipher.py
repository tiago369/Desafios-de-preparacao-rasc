def caeser_cipher(txt):
    txt2 = ''
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c']
    alphaM = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C']
    for i in range(0, len(txt), 1):
        for j in range(0, len(alphabet)-3,1):
            if(txt[i] == alphabet[j]):
                txt2 += alphabet[j+3]
            elif(txt[i] == alphaM[j]):
                txt2 += alphaM[j+3]
    return txt2

def deco_caeser_cipher(txt):
    txt2 = ''
    alphabet = ['x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alphaM = ['X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in range(0, len(txt), 1):
        for j in range(0, len(alphabet)-3,1):
            if(txt[i] == alphabet[j]):
                txt2 += alphabet[j-3]
            elif(txt[i] == alphaM[j]):
                txt2 += alphaM[j-3]
    return txt2

x = int(input('Se você deseja encriptar a mensagem digite 1, se deseja descriptar digite 0: '))
t = str(input('Digite o texto: '))
if(x == 1):
    print(caeser_cipher(t))
elif(x == 0):
    print(deco_caeser_cipher(t))
else:
    print('Digite 1 ou 0')
