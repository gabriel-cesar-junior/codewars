def usuario():
    usu = lambda nome, idade: print(f'{nome} possui {idade} anos')
    return usu('joao',17)
print(usuario())