
def separar(lista):
    lista_par=[]
    lista_impar=[]

    for numero in lista:
        if numero%2==0:
            lista_par.append(numero)
        else:
            lista_impar.append(numero)
    
    lista_par.sort()
    lista_impar.sort()

    return lista_par, lista_impar

pares, impares = separar([6,5,2,1,7])

print(pares)
print(impares)