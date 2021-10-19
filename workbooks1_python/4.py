def capitalize(text):
    text = text[0].upper() + text[1:]
    tam = len(text)
    for i in range(1, tam-2, 1):
        if(text[i] == 'i' and text[i-1] == ' ' and text[i+1] == ' '):
            text = text[:i] + 'I' + text[i+1:]
        elif(text[i] == '.' or text[i] == '!' or text[i] == '?'):
            if(text[i+1] == ' '):
                text = text[:i+2] + text[i+2].upper() + text[i+3:]
            else:
                text = text[:i] + text[i+1].upper() + text[i+2:]
    return text

t = str(input('Escreva o texto a ser capitalizado: '))
print(capitalize(t))
