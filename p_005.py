print('-'*10,'Primer Ejercicio','-'*10)
def greet_user(name):
  print(f'Hola {name}, bienvenido!')
greet_user('Juan')

#----------------------------------------------------------------  
for i in range(5):
  print('')
print('-'*10,'Segundo Ejercicio','-'*10)

def calculate_area(radio):
  area = round((3.1416*(radio**2)), 2)
  return area

area = calculate_area(5)
print(f'El área del círculo es: {area}')

#----------------------------------------------------------------  
for i in range(5):
  print('')
print('-'*10,'Tercer Ejercicio','-'*10)

numbers = [12, 45, 23, 67, 89, 34]

def find_max(numeros):
  return max(numeros)

max_number = find_max(numbers)
print(f'El número máximo en la lista es: {max_number}')

#----------------------------------------------------------------  
for i in range(5):
  print('')
print('-'*10,'Cuarto Ejercicio','-'*10)

def is_prime(numero):
  iteraciones = 0
  valor = { numero: True}
  for i in range(round(numero**0.5)):
    if numero % (i + 1) == 0:
      iteraciones += 1
  print (iteraciones)
  if(iteraciones > 1):
    valor[numero] = False
  return valor

result = is_prime(4)
for item, valor in result.items():
  print(f'¿{item} es primo? {valor}')

#----------------------------------------------------------------  
for i in range(5):
  print('')
print('-'*10,'Quinto Ejercicio','-'*10)

def reverse_string(texto):
  print(f'Cadena original: {original_string}\nCadena invertida: {texto[::-1]}')
original_string = 'Python'
reversed_string = reverse_string(original_string)

#----------------------------------------------------------------  
for i in range(5):
  print('')
print('-'*10,'Primer Ejercicio','-'*10)

entrada =  [42, 15, 7, 89, 23, 56, 11, 98, 30, 5]

def suma(numeros):
  pares = [num for num in numeros if num % 2 == 0]
  print(sum(pares))
  return pares

pares = suma(entrada)

#----------------------------------------------------------------  
for i in range(5):
  print('')
print('-'*10,'Segundo Ejercicio','-'*10)

from collections import Counter
texto = 'Había una vez en un pequeño pueblo al pie de las montañas, una biblioteca olvidada. En sus estantes polvorientos, los libros susurraban historias del pasado. Un día, una joven curiosa llamada Isabella descubrió el lugar escondido. Entre las páginas amarillentas y desgastadas, encontró un antiguo diario que narraba misteriosas aventuras de un explorador perdido. Emocionada por la posibilidad de desentrañar secretos olvidados, Isabella se embarcó en su propia búsqueda, llevando consigo las historias encerradas en aquel rincón tranquilo del pueblo.'
def word_counter(text):
  words = []
  word = ''
  for i in text:
    if i in ' ,.' and word != '':
      words.append(word)
      word = ''
    else:
      if i != ' ':
        word += i
  frequency = Counter(words)
  return frequency

palabras = word_counter(texto)

for item, valor in palabras.items():
  print(f'Frecuencia: {valor} || Palabra: {item}')

#----------------------------------------------------------------  
for i in range(5):
  print('')
print('-'*10,'Tercer Ejercicio','-'*10)

lista_palabras = ["montaña", "aventura", "tesoro", "sueño", "misterio", "viaje", "descubrimiento", "imaginación", "caminata", "destino"]

def reverse_words(words):
  reverse = {word: word[::-1] for word in words}
  return reverse

reverse = reverse_words(lista_palabras)
for item, valor in reverse.items():
  print(f'Palabra: {item} || Inverso: {valor}')

#----------------------------------------------------------------  
for i in range(5):
  print('')
print('-'*10,'Cuarto Ejercicio','-'*10)

def calculo_factorial(num):
  factorial = 1
  for i in range(num):
    factorial = factorial*(i+1)
  return factorial

numero_factorial = calculo_factorial(0)
print(numero_factorial)

#----------------------------------------------------------------  
for i in range(5):
  print('')
print('-'*10,'Quinto Ejercicio','-'*10)

import re

def validar_contraseña(contraseña):
    # Longitud mínima
    if len(contraseña) < 8:
        return False, "La contraseña debe tener al menos 8 caracteres."

    # Presencia de números y caracteres especiales
    if not any(char.isdigit() for char in contraseña) or not any(char.isalnum() for char in contraseña):
        return False, "La contraseña debe contener al menos un número y un carácter especial."

    # Diversidad de caracteres (mayúsculas y minúsculas)
    if not any(char.isupper() for char in contraseña) or not any(char.islower() for char in contraseña):
        return False, "La contraseña debe contener tanto letras mayúsculas como minúsculas."

    # Evitar palabras comunes (opcional, puedes personalizar esta lista)
    palabras_comunes = ['password', '123456', 'qwerty']
    if any(palabra in contraseña.lower() for palabra in palabras_comunes):
        return False, "La contraseña no debe contener palabras comunes."

    return True, "Contraseña válida."

# Ejemplo de uso
contraseña_usuario = input("Ingrese su contraseña: ")
es_valida, mensaje = validar_contraseña(contraseña_usuario)

if es_valida:
    print("¡Contraseña aceptada!")
else:
    print(f"Error: {mensaje}")
