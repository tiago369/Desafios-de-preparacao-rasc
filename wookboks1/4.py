def capitalize(text):
    text2 = ""
    str(text2)
    text = text.capitalize()
    tam = len(text)
    for i in range(0, tam-1, 1):
        if(text[i] == 'i' and text[i-1] == ' ' and text[i+1] == ' '):
            text2 = text[:i-1] + 'I' + text[i+1:]
            text = text2
        elif(text[i] == '.' or text[i] == '!' or text[i] == '?'):
            if(text[i+1] == ' '):
                text2 = text[:i+1] + text[i+2].upper + text[i+3:]
                text = text2
            else:
                text2 = text[:i] + text[i+1].upper + text[i+2:]
                text = text2
    return text

t = str(input('->'))
print(capitalize(t))
