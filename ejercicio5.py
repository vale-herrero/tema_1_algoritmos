import sys

argumentos = sys.argv

numero_argumentos=len(argumentos)

if numero_argumentos==0:
    print("ingrese un numero entero positivo")
else: 
    numero= argumentos[0]
    unidades= '000'+numero[-1]
    decenas= '00'+numero[-2]+'0'
    centenas='0'+numero[-3]+'00'
    miles= numero[-4]+'000'

    print(unidades)
    print(decenas)
    print(centenas)
    print(miles)