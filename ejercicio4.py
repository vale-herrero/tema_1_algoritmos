tareas= ["A", "B", "C", "D", "E"]
prioridad= [4, 3, 1, 5, 2]

tuplas=list(zip(tareas,prioridad))

orden= lambda tupla: tupla[1]
tuplas_ordenadas=sorted(tuplas, key=orden)
lista_ordenada=[]
for tupla in tuplas_ordenadas:
    lista_ordenada.append(tupla[0])

print(lista_ordenada)