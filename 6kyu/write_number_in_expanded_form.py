def expanded_form(num):
    num = str(num)
    lista = []
    for i in range(len(num)):
        if num[i] != '0':
            x= 10**int(len(num[i:])-1)
            resultado = str(x*int(num[i]))
            lista.append(resultado)
    return '+'.join(lista)
    
print(expanded_form(521))