# Tema 2: Tipos de datos en python
# 2.5 Listas

# Las listas se utilizan para almacenar varios elementos en una sola variable.
# Los elementos de una lista están ordenados, son modificables y permiten valores duplicados:
#   --> Los elementos tienen un orden definido y ese orden no cambiará. 
#   --> Los elementos establecidos no pueden ser cambiados, pero si se pueden eliminar y/o agregar elementos.
#   --> Si se agregan nuevos elementos, los nuevos elementos se colocan al final de la lista.
#   --> Es posible cambiar, agregar y eliminar elementos en una lista después de haberla creado.
#   --> Los elementos están indexados, el primer elemento tiene el índice [0], el segundo índice [1], etc
#   --> Dado que las listas están indexadas, las listas pueden tener elementos con el mismo valor (duplicados).

# Las listas se crean usando corchetes
print("las listas en python se definen utilizando corchetes")
my_list1 = ["apple", "banana", "cherry"]
print(my_list1)
print('')

# tambien se puede definir una lista utilizando el constructor list()
print("usando el constructor list() para crear una lista")
thislist = list(("apple", "banana", "cherry")) 
print(thislist)
print('')

# Las listas pueden contener cualquier tipo de datos, inlcuso otras listas
print("las listas pueden contener cualquier tipo de dato")
list1 = [True, "apple", 5, "banana", 7, "cherry", 3, False, [1,2,3]]
print(list1)
print('')

# Listas permiten valores duplicados
print("Las listas permiten valores duplicados")
my_list2 = ["apple", "banana", 5, "cherry", "apple", "cherry", 5]
print(my_list2)
print('')

# Para determinar cuántos elementos tiene una lista, se utiliza la función len()
print("uso de la funcion len() para determinar el número elementos de una lista")
print(f"la lista {my_list2} tiene un total de {len(my_list2)} elementos")
print('')

# Para determinar si un elemento específico está presente en una lista, se utiliza la palabra clave in.
print("verificando si un elemento especifico se encuentra en una lista")
my_list3 = ["apple", "banana", "cherry"]
print(f"Verificando si apple se encuentra presente en la lista: {'apple' in my_list3}")
print('')

# ----------------------------------------------------------------------------------------------------------------------------------------
# ACCEDIENDO A ELEMENTOS ESPECIFICOS DE UNA LISTA
print("\nACCEDIENDO A ELEMENTOS ESPECIFICOS DE UNA LISTA\n")
# Los elementos de la lista se encuentran indexados, por lo tanto, pueden ser accedidos consultando el número de índice correspondiente
print('accediendo a elementos especificos de una lista')
list2 = ["apple", "banana", "cherry"]   # el primer elemento tiene el índice [0], el segundo índice [1], etc
print(f"accediendo al segundo  elemento de la lista {list2}: {list2[1]}")
print('')

# python permite la indexacion negativa, lo que significa comenzar desde el final. -1 se refiere al último elemento, -2 se refiere al penúltimo elemento, etc.
print('indexación negativa de listas en python')
print(f"accediendo al último elemento de la lista {list2}: {list2[-1]}")
print('')

# Las listas permiten especificar un rango de índices, indicando el inicio y el final.
# Al especificar un rango, el valor que se retorna es una nueva lista con los elementos especificados.
print("Las listas permiten especificar un rango de índices")
list3 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(f"Accediendo desde el tercer hasta el quinto elemento de la lista {list3}: {list3[2:5]}") # La búsqueda comienza en el índice 2 (incluido) y finaliza en el índice 5 (no incluido).
print('')

# Al omitir el valor inicial, el rango comenzará en el primer elemento.
print("Si no se especifica el índice inicial, el rango comenzará en el primer elemento")
print(f"Accediendo desde el primer hasta el cuarto elemento de la lista {list3}: {list3[:4]}") # La búsqueda comienza desde el primer elemento (incluido) y finaliza en el índice 4 (no incluido).
print('')

# Al omitir el valor final, el rango continuará hasta el final de la lista.
print("Si no se especifica el índice final, el rango comenzará desde el elemento especificado hasta el final")
print(f"Accediendo desde el tercer hasta el último elemento de la lista {list3}: {list3[2:]}") # La búsqueda comienza desde el tercer elemento (incluido) y continúa hasta el final de la lista.
print('')

# Al especificar índices negativos, la búsqueda se inicia desde el final de la lista.
print("Si se especifican índices negativos, la búsqueda se inicia desde el final")
print(f"Accediendo desde el segundo hasta el penúltimo elemento de la lista {list3}: {list3[-6:-1]}") # La búsqueda comienza en el índice -6 (incluido) y finaliza en el índice -2 (no incluido).
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CAMBIANDO ELEMENTOS DENTRO DE UNA LISTA
print("\nCAMBIANDO ELEMENTOS DENTRO DE UNA LISTA\n")
# para cambiar el valor de un elemento especifico, se debe consultar el número del indice}
print("Para cambiar el valor de un elemento en una lista, se debe consultar el número del indice")
thislist = ["apple", "banana", "cherry"]
print(f"cambiando el segundo elemento de la lista: {thislist}")
thislist[1] = "mango"
print(f"lista modificada: {thislist}")
print('')

# Para cambiar el valor de los elementos dentro de un rango específico, se debe definir una lista con los nuevos valores y consultar el rango de números de índice donde se desea insertar los nuevos valores.
print("Para cambiar varios elementos de una lista, se debe consultar el rango específico que se desea cambiar y asignarle los nuevos valores mediante otra lista")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(f"Cambiando el segundo y tercer elemento de la lista: {thislist}")
thislist[1:3] = ["blackcurrant", "watermelon"]
print(f"Lista modificada: {thislist}")
print('')

# Si se insertan más elementos de los que se desean reemplazar, los nuevos elementos se insertarán donde se especificó y los elementos restantes se moverán en consecuencia
# Sin embargo, la longitud de la lista cambiará cuando la cantidad de elementos insertados no coincida con la cantidad de elementos reemplazados.
print("Si se insertan más elementos de los que se reemplazan, los nuevos elementos se insertan donde se especificó y los elementos restantes se mueven en consecuencia")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(f"Cambiando el segundo y tercer elemento de la lista: {thislist}")
thislist[1:3] = ["blackcurrant", "watermelon", "lemon"]
print(f"Lista modificada: {thislist}")
print('')

# Si se insertan menos elementos de los que se desean reemplazar, los nuevos elementos se insertarán donde se especificó y los elementos restantes se moverán en consecuencia:
print("Si se insertan menos elementos de los que se reemplazan, los nuevos elementos se insertan donde se especificó y los elementos restantes se mueven en consecuencia")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(f"Cambiando el segundo y tercer elemento de la lista: {thislist}")
thislist[1:3] = ["lemon"]
print(f"Lista modificada: {thislist}")
print('')

# Para insertar un nuevo elemento de la lista, sin reemplazar ninguno de los valores existentes, se utiliza el método insert().
# El método insert() inserta un elemento en el índice especificado:
thislist = ["apple", "banana", "cherry"]
print("Usando el metodo insert() para agregar un nuevo elemento a una lista en un indice especifico")
print(f"Agregando un nuevo elemento en el indice 2 de la lista: {thislist}")
thislist.insert(2, "watermelon")
print(f"lista modificada: {thislist}")
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# AGREGANDO ELEMENTOS A UNA LISTA
print("\nAGREGANDO ELEMENTOS A UNA LISTA\n")
# Para agregar un elemento al final de una lista, se utiliza el método append():
print("Usando el metodo para() para agregar nuevos elementos al final de una lista")
thislist = ["apple", "banana", "cherry"]
print(f"Agregando un nuevo elemento a la lista: {thislist}")
thislist.append("orange")
print(f"lista modificada: {thislist}")
print('')

# Para agregar elementos de otra lista a la lista actual, se utiliza el método extend().
print("Usando el método extend() para agregar nuevos elementos a una lista")
aux_list= ["mango", "lemon"]
print(f"Agregando los elementos de {aux_list} a la lista: {thislist}")
thislist.extend(aux_list)
print(f"lista modificada: {thislist}")
print('')

# El método extend() no solo agrega listas, tambien puede agregar cualquier objeto iterable (tuplas, conjuntos, diccionarios, etc.).
print("El método extend() permite agregar cualquier objeto iterable")
aux_iter = ('lemon', 'mango')
thislist = ["apple", "banana", "cherry"]
print(f"Agregando el iterable {aux_iter}  a la lista: {thislist}")
thislist.extend(aux_iter)
print(f"lista modificada: {thislist}")
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ELIMINANDO ELEMENTOS DE UNA LISTA
print("\nELIMINANDO ELEMENTOS DE UNA LISTA\n")
# Para elminar un elemento especifico de una lista, se utiliza el método remove()
print("usando el metodo remove() para eliminar elementos de una lista")
thislist = ["apple", "banana", "cherry"]
print(f"Eliminando el elemento 'banana' de la lista: {thislist}")
thislist.remove("banana")
print(f"lista modificada: {thislist}")
print('')

# Si hay más de un elemento con el valor especificado, el método remove() elimina el primero de ellos
print("si hay mas de un elemento con el valor especificado, el método remove() elimina el primero de ellos")
thislist = ["apple", "banana", "lemon", "cherry", "banana"]
print(f"Eliminando el primer elemento 'banana' de la lista: {thislist}")
thislist.remove("banana")
print(f"lista modificada: {thislist}")
print('')

# para eliminar un elemento en un indice especifico se utiliza el método pop()
print("usando el metodo pop() para eliminar un elemento especifico de una lista")
thislist = ["apple", "banana", "lemon", "cherry", "banana"]
print(f"Eliminando el elemento 'lemon' de la lista: {thislist}")
thislist.pop(2)
print(f"lista modificada: {thislist}")
print('')

# Si no especifica el índice, el método pop() elimina el último elemento
print("usando el metodo pop() para eliminar el último elemento de una lista")
thislist = ["apple", "banana", "lemon", "cherry", "banana"]
print(f"Eliminando el último elemento de la lista: {thislist}")
thislist.pop()
print(f"lista modificada: {thislist}")
print('')

# para eliminar un elemento en un indice especifico tambien puede utilizarse la palabra clave del
print("usando la palabra clave del para eliminar un elemento especifico de una lista")
thislist = ["apple", "banana", "cherry"]
thislist = ["apple", "banana", "lemon", "cherry", "banana"]
print(f"Eliminando el elemento 'lemon' de la lista: {thislist}")
del thislist[2]
print(f"lista modificada: {thislist}")
print('')

# para eliminar una lsita completamente se utiliza la aplabra clave del
print("eliminando completamente una lista")
print(f"eliminando la lista: {thislist}")
del thislist
print('')