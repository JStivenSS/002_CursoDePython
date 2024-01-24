'''
potencias = {i: i * 3 for i in range(1,5)}
print(potencias)

countries = [
    "Afganistán", "Albania", "Alemania", "Andorra", "Angola", "Antigua y Barbuda", "Arabia Saudita", 
    "Argelia", "Argentina", "Armenia", "Australia", "Austria", "Azerbaiyán", "Bahamas", "Bangladés", 
    "Barbados", "Baréin", "Bélgica", "Belice", "Benín", "Bielorrusia", "Birmania", "Bolivia", "Bosnia y Herzegovina", 
    "Botsuana", "Brasil", "Brunéi", "Bulgaria", "Burkina Faso", "Burundi", "Bután", "Cabo Verde", "Camboya", 
    "Camerún", "Canadá", "Catar", "Chad", "Chile", "China", "Chipre", "Ciudad del Vaticano", "Colombia", 
    "Comoras", "Corea del Norte", "Corea del Sur", "Costa de Marfil", "Costa Rica", "Croacia", "Cuba", 
    "Dinamarca", "Dominica", "Ecuador", "Egipto", "El Salvador", "Emiratos Árabes Unidos", "Eritrea", 
    "Eslovaquia", "Eslovenia", "España", "Estados Unidos", "Estonia", "Etiopía", "Filipinas", "Finlandia", 
    "Fiyi", "Francia", "Gabón", "Gambia", "Georgia", "Ghana", "Granada", "Grecia", "Guatemala", "Guyana", 
    "Guinea", "Guinea-Bisáu", "Guinea Ecuatorial", "Haití", "Honduras", "Hungría", "India", "Indonesia", 
    "Irak", "Irán", "Irlanda", "Islandia", "Islas Marshall", "Islas Salomón", "Israel", "Italia", "Jamaica", 
    "Japón", "Jordania", "Kazajistán", "Kenia", "Kirguistán", "Kiribati", "Kuwait", "Laos", "Lesoto", 
    "Letonia", "Líbano", "Liberia", "Libia", "Liechtenstein", "Lituania", "Luxemburgo", "Macedonia del Norte", 
    "Madagascar", "Malasia", "Malaui", "Maldivas", "Malí", "Malta", "Marruecos", "Mauricio", "Mauritania", 
    "México", "Micronesia", "Moldavia", "Mónaco", "Mongolia", "Montenegro", "Mozambique", "Namibia", 
    "Nauru", "Nepal", "Nicaragua", "Níger", "Nigeria", "Noruega", "Nueva Zelanda", "Omán", "Países Bajos", 
    "Pakistán", "Palaos", "Panamá", "Papúa Nueva Guinea", "Paraguay", "Perú", "Polonia", "Portugal", 
    "Reino Unido", "República Centroafricana", "República Checa", "República del Congo", "República Democrática del Congo", 
    "República Dominicana", "Ruanda", "Rumania", "Rusia", "Samoa", "San Cristóbal y Nieves", "San Marino", 
    "San Vicente y las Granadinas", "Santa Lucía", "Santo Tomé y Príncipe", "Senegal", "Serbia", "Seychelles", 
    "Sierra Leona", "Singapur", "Siria", "Somalia", "Sri Lanka", "Suazilandia", "Sudáfrica", "Sudán", 
    "Sudán del Sur", "Suecia", "Suiza", "Surinam", "Tailandia", "Tanzania", "Tayikistán", "Timor Oriental", 
    "Togo", "Tonga", "Trinidad y Tobago", "Túnez", "Turkmenistán", "Turquía", "Tuvalu", "Ucrania", "Uganda", 
    "Uruguay", "Uzbekistán", "Vanuatu", "Venezuela", "Vietnam", "Yemen", "Yibuti", "Zambia", "Zimbabue"
]

lengths = {i: len(i) for i in countries}

for pais, longitud in lengths.items():
    print(f'País: {pais} || Longitud: {longitud} \n')


import random
import string

def generar_palabra_aleatoria(longitud):
    caracteres = string.ascii_lowercase  # Letras minúsculas
    palabra_aleatoria = ''.join(random.choice(caracteres) for _  in range(longitud))
    return palabra_aleatoria

random_words = {i: generar_palabra_aleatoria(8) for i in range(5)}
print(random_words) 

frutas = ['Manzana', 'Banana', 'Cereza', 'Dátiles', 'Uva', 'Kiwi', 'Naranja', 'Pera', 'Melón', 'Fresa']
precios = [2.5, 1.8, 3.0, 5.5, 4.2, 2.0, 2.9, 3.5, 6.8, 4.0]

fruit_prices = {frutas: precios for (frutas, precios) in zip(frutas, precios)}
print(fruit_prices)

nombres = ['Ana', 'Juan', 'María', 'Carlos', 'Luis', 'Elena', 'Pedro', 'Laura', 'Miguel', 'Sofía']
edades = [25, 30, 22, 35, 28, 24, 40, 26, 32, 29]

name_lengths = {nombres: edades for (nombres, edades) in zip(nombres, edades)}
print(name_lengths)
'''

estudiantes = ['Ana', 'Juan', 'María', 'Carlos', 'Luis']
calificaciones = [85, 92, 78, 95, 89]

notas = {nombre: nota for (nombre, nota) in zip(estudiantes, calificaciones)}

for nombre, nota in notas.items():
  print(f'Nombre: {nombre} || Nota: {nota}')


for i in range(5):
  print('')

from collections import Counter
texto = "programacion en python"

frecuencia = Counter(texto)

for letra, fre in frecuencia.items():
  print(f'Letra: {letra} Apariciones: {fre}')

for i in range(5):
  print('')

productos = ['Manzanas', 'Leche', 'Pan', 'Huevos']
precios = [2.5, 1.0, 0.8, 0.2]
cantidades = [3, 2, 1, 12]

compras = {producto: {'precio': precio, 'cantidad': cantidad} for (producto, precio, cantidad) in zip (productos, precios, cantidades)}

for producto, detalles in compras.items():
  print(f'Producto: {producto}')
  for item, valor in detalles.items():
    print(f'{item}: {valor}')

for i in range(5):
  print('')

ciudades = ['Bogotá', 'Lima', 'Madrid', 'Nueva York']
temperaturas_celsius = [15, 25, 30, 10]

temperaturas = {ciudad: temperatura*9/5+32 for (ciudad, temperatura) in zip(ciudades, temperaturas_celsius)}

for ciudad, Fahrenheit in temperaturas.items():
  print(f'Ciudad: {ciudad} | Grados Fahrenheit: {Fahrenheit}')

for i in range(5):
  print('')

nombres_estudiantes = ['Ana', 'Juan', 'María', 'Carlos', 'Luis']
edades_estudiantes = [22, 24, 21, 25, 23]
notas_estudiantes = [85, 92, 78, 95, 89]

datos_estudiantes = {nombre: {'edad': edad, 'nota': nota} for (nombre, edad, nota) in zip(nombres_estudiantes, edades_estudiantes, notas_estudiantes)}

for nombre, detalles in datos_estudiantes.items():
  print(f'Nombre: {nombre}')
  for item, valor in detalles.items():
    print(f'{item}: {valor}')