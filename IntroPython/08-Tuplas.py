'''
Las tuplas son inmutables
se crea con ()
Las tuplas son secuencias de elementos
'''
tupla = ("uno","dos","tres")
print(tupla)
#Puede ser de cualquier tipo
tuplasVariosDtos = (12,True,23.5,"El gato", 12+4j)
print(tuplasVariosDtos)
#puede tener una tupla dentro de otra tupla
tuplasConTuplas=(1,2,3,4,(1,2,3))
print(tuplasConTuplas)
#paraimprimir con un solo dato
print(tuplasVariosDtos[3])
print(tuplasVariosDtos[-2])
print(tuplasVariosDtos[0:2])
a,b,c = tupla
print(a,b,c)