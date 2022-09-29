
def agregar_una_vez(lista, el):

    if el in lista:
        try: 
            raise ValueError()
        except ValueError as err:
            print(f'imposible añadir elementos duplicados => {el}')
    else:
        lista.append(el)
        print(lista)

lista1=[1,5,-2]
elemento= 10
lista_resultado = agregar_una_vez(lista1,elemento)
