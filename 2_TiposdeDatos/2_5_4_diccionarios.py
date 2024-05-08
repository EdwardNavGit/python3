# Tema 2: Tipos de datos en python
# 2.5.4 diccionarios

# Los diccionarios se utilizan para almacenar valores de datos en pares clave:valor.
# Un diccionario es una colección ordenada, modificable y que no permite duplicados.
#   --> los elementos de un diccionario tienen un orden definido y ese orden no cambiará.
#   --> Es posible cambiar, agregar y eliminar elementos a un diccionario después de haberlo creado.
#   --> Los diccionarios no pueden tener dos elementos con la misma clave, los valores duplicados sobrescribirán los valores existentes.
#   --> Los elementos de un diccionario se presentan en pares clave:valor y se puede hacer referencia a ellos mediante el nombre de la clave.

# ----------------------------------------------------------------------------------------------------------------------------------------
# DEFINIENDO UN DICCIONARIO EN PYTHON
print("\nDEFINIENDO DICCIONARIOS\n")

# Los diccionarios se definen utilizando llaves {} y tienen claves y valores
print("los diccionarios en en Python se definen utilizando llaves {} y sus elementos se definen mediante pares clave:valor")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(f"Diccionario en Python: {thisdict}, Tipo de dato: {type(thisdict)}")
print('')

# También se puede definir un diccionario utilizando el constructor dict()
print("También se puede definir un diccionario utilizando el constructor dict():")
thisdict = dict(name = "John", age = 36, country = "Norway")
print(f"Diccionario en Python: {thisdict}, Tipo de dato: {type(thisdict)}")
print('')

# Los diccionarios pueden contener cualquier tipo de dato, incluso otros diccionarios
print("Los diccionarios pueden contener cualquier tipo de dato:")
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"],
  "owner": {
      "name": 'juanito',
      "years": 32
  }
}
print(f"Diccionario con diferentes tipos de datos: {thisdict}")
print('')

# Los diccionarios no pueden tener dos elementos con la misma clave, los valores duplicados sobrescribirán los valores existentes:
print("Los diccionarios no permiten elementos duplicados, los valores duplicados sobreescribiran los valores existentes")
str_dict= "{'brand': 'Ford','model': 'Mustang','year': 1964,'year': 2020}"
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(f"intentado agregar claves duplicadas a un diccionario: {str_dict}")
print(f"Diccionario resultante: {thisdict}")
print('')

# ----------------------------------------------------------------------------------------------------------------------------------------
# ACCEDIENDO A ELEMENTOS DE UN DICCIONARIO
print("\nACCEDIENDO A ELEMENTOS DE UN DICCIONARIO\n")

# Para determinar si una clave especifica está presente en un diccionario, se utiliza la palabra clave in.
print("Verificando si una clave específica se encuentra en un diccionario:")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
result = 'brand' in thisdict
print(f"Verificando si 'brand' se encuentra presente en el diccionario {thisdict}, resultado: {result}")
print('')

# Para acceder a los elementos de un diccionario se debe consultar su nombre clave, entre corchetes []. Sin embargo, si la clave no está presente en el diccionario se presentará un error.
print("Accediendo a elementos de un diccionario mediante su clave utilizando []")
print(f"El valor del elemento con palabra clave 'year' del diccionario {thisdict} es: {thisdict['year']}")
print('')

# El método get() permite obtener también los elementos de un diccionario a partir de su clave. Sin embargo, este método permite devolver un valor por defecto en caso de que dicha clave no exista.
print("El método get() se utiliza para acceder a elementos de un diccionario mediante su clave. Si la clave no existe se puede colocar un valor por defecto.")
print(f"El valor del elemento con palabra clave 'model' del diccionario {thisdict} es: {thisdict.get('model')}")
print(f"El valor del elemento con palabra clave 'owner' del diccionario {thisdict} es: {thisdict.get('owner', 'No encontrado')}")
print('')

# El método keys() permite obtener una lista de todas las claves presentes en un diccionario.
# La lista de claves es una vista del diccionario, lo que significa que cualquier cambio realizado en el diccionario se reflejará en la lista de claves.
print("El método keys() permite obtener una lista de todas las claves presentes en un diccionario.")
keys = thisdict.keys()
print(f"Las claves presentes en el diccionario {thisdict} son: {keys}")
print('')

# El método values() permite obtener una lista de todas los valores presentes en un diccionario.
# La lista de valores es una vista del diccionario, lo que significa que cualquier cambio realizado en el diccionario se reflejará en la lista de valores.
print("El método values() permite obtener una lista de todos los valores presentes en un diccionario.")
values = thisdict.values()
print(f"Los valores presentes en el diccionario {thisdict} son: {values}")
print('')

# El método items() permite obtener los elementos de un diccionario, como una lista de tuplas.
# La lista de elementos es una vista del diccionario, lo que significa que cualquier cambio realizado en el diccionario se reflejará en la lista de elementos.
print("El método items() permite obtener los elementos de un diccionario como una lista de tuplas.")
items = thisdict.items()
print(f"Los elementos (items) presentes en el diccionario {thisdict} son: {items}")
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CAMBIANDO ELEMENTOS DE UN DICCIONARIO
print("\nCAMBIANDO ELEMENTOS DE UN DICCIONARIO\n")

# Para cambiar el valor de un elemento en un diccionario, se debe consultar su clave.
print("Para cambiar el valor de un elemento en una lista, se debe consultar su clave.")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(f"Cambiando el elemento con clave 'year' del diccionario: {thisdict}")
thisdict['year'] = 1980
print(f"Diccionario modificado: {thisdict}")
print('')

# El método update() permite actualizar un diccionario con los elementos del argumento dado. El argumento debe ser un diccionario o un objeto iterable con pares clave:valor.
# Si la clave no existe, se creará en el diccionario.
print("El método update() se utiliza para actualizar un diccionario con otro iterable con pares clave:valor.")
iterable = {"year": 2020}
print(f"Actualizando el diccionario {thisdict} con el iterable {iterable}")
thisdict.update(iterable)
print(f"Diccionario modificado: {thisdict}")
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# AGREGANDO ELEMENTOS A UN DICCIONARIO
print("\nAGREGANDO ELEMENTOS A UN DICCIONARIO\n")

# Para agregar un nuevo elemento a un diccionario se debe crear una nueva clave y asignarle un valor.
print("Para agregar un nuevo elemento a un diccionario se debe crear una nueva clave con su valor correspondiente.")
print(f"Agregando el elemento 'owner':'jose' al diccionario {thisdict}")
thisdict['owner'] = 'jose'
print(f"Diccionario modificado: {thisdict}")
print('')

# El método update() también permite agregar nuevos elementos a un diccionario existente. El argumento debe ser un diccionario o un objeto iterable con pares clave:valor.
print("El método update() también se puede utilizar para agregar nuevos elementos a un diccionario existente.")
iterable = {"color": 'red'}
print(f"Agregando el iterable {iterable} al diccionario {thisdict}")
thisdict.update(iterable)
print(f"Diccionario modificado: {thisdict}")
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ELIMINANDO ELEMENTOS DE UN DICCIONARIO
print("\nELIMINANDO ELEMENTOS DE UN DICCIONARIO\n")

# El método pop() elimina el elemento con el nombre de clave especificado
print("El método pop() se utiliza para eliminar un elemento específico mediante su clave.")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(f"Eliminando el elemento con clave 'model' del diccionario {thisdict}")
thisdict.pop("model")
print(f"Diccionario modificado: {thisdict}")
print('')

# El método popitem() elimina el último elemento de un diccionario
print("El método popitem() elimina el último elemento de un diccionario.")
print(f"Eliminando el último elemento del diccionario {thisdict}")
thisdict.popitem()
print(f"Diccionario modificado: {thisdict}")
print('')

# La palabra clave 'del' elimina el elemento con el nombre de clave especificado
print("La palabra clave 'del' elimina el elemento con el nombre de clave especificado.")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(f"Eliminando el elemento con clave 'model' del diccionario {thisdict}")
del thisdict["model"]
print(f"Diccionario modificado: {thisdict}")
print('')

# El método clear() se utiliza para vaciar el contenido de un diccionario. El diccionario aún permanece, pero no tiene contenido.
print("El método clear() se utiliza para vaciar un diccionario.")
print(f"Eliminando el contenido del diccionario: {thisdict}")
thisdict.clear()
print(f"Diccionario modificado: {thisdict}")
print('')

# Para eliminar un diccionario completamente, se utiliza la palabra clave del.
# Esto libera la memoria asociada, lo que puede ser útil en programas con grandes cantidades de datos.
print("La palabra clave del también se utiliza para eliminar completamente un diccionario.")
print(f"Eliminando el diccionario: {thisdict}")
del thisdict
print('')

