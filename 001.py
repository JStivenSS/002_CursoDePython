set_a = {'col', 'mex', 'bra', 'arg', 'chi'}
set_b = {'col', 'mex', 'per', 'ecu', 'bol'}

#Une dos diccionarios, agregando una sola vez cada elemento
set_c = set_a.union(set_b)
print(f'Union de conjuntos con.union \n{set_c}')
print(f'Union de conjuntos utilizando | \n{set_a | set_b}\n')

#Muestra los datos del diccionario que estan compartidos
set_d = set_a.intersection(set_b)
print(f'Interseccion utilizando .intersection \n{set_d}')
print(f'Interseccion utilizando & \n{set_a & set_b}\n')

#Muestra los datos que no tiene en comun
set_e = set_a.difference(set_b)
print(f'Diferencia utilizando .difference \n{set_e}')
print(f'Diferencia utilizando - \n{set_a - set_b}\n')

#Muestra los datos que no tienen en comun los diccionarios
set_f = set_a.symmetric_difference(set_b)
print(f'Diference symetric utilizando: symmetric_diference: \n{set_f}')
print(f'Diference symetric utilizando: ^ \n{set_a ^ set_b}\n')

#--Ejemplo numero dos con diferentes diccionarios--
countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

#Ejemplo de que union se puede utilizar con varios diccionarios, aplicaria con el resto
new_set = countries.union(northAm, centralAm, southAm)
print(f'Union de varios conjuntos con .union \n{new_set}')