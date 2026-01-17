'''
Una lista es una secuencia de elementos.
se crea con []
'''
lista1 = ["Diario", 33,9.5,"German",20.8]
#Es para imprimir la lista completa
print(lista1)
print(lista1[:])
#Es para imprimir solo el primer elemento
print(lista1[1])
print(lista1[-1])
#Es para imprimir solo los elementos de la lista
print(lista1[0:3])
print(lista1[3:])

#para extender la lista
lista1.append("Vargas")
print(lista1)
#para insertar un elemento en una posicion
lista1.insert(2,"Nadia")
print(lista1)
#para extender la lista con un elemento
lista1.extend(["uno",1.1,False])
print(lista1)
#para borrar un elemento
lista1.remove(33)
print(lista1)
#para borrar un elemento en una posicion
lista1.pop()
print(lista1)
#crear otra lista y concatenarla con la anterior
lista2 = ["tres","cuatro"]
lita3 = lista1 + lista2
print(lita3)
#para imprimir cuatro veces la lista
print(lista2*4)
lista4 = [2,1,5,4,3]
print(lista4)
#ordenar la lista
lista4.sort()
print(lista4)