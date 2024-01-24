#-------------------------------------------------
print('-'*10, 'Primer Ejercicio', '-'*10)
original_numbers = [1, 2, 3, 4, 5]
squared_numbers = {i: i*i for i in original_numbers}

for item, valor in squared_numbers.items():
  print(f'Numero: {item}  || Su cuadrado es: {valor}')

#-------------------------------------------------
for i in range(5):
  print('')
print('-'*10, 'Segundo Ejercicio', '-'*10)

text = 'Python es un Lenguaje de Programación'

uppercase_counts = {i: text.count(i) for i in text if i==i.upper() and i != ' '}

for item, valor in uppercase_counts.items():
  print(f'Letra: {item} || Apariciones: {valor}')

#-------------------------------------------------
for i in range(5):
  print('')
print('-'*10, 'Tercer Ejercicio', '-'*10)

import random
random_numbers = [random.randint(1, 10) for _ in range(5)]

squares = [square**2 for square in random_numbers]

for i in range(len(random_numbers)):
  print(f'Numero: {random_numbers[i]} || Su cuadrado es: {squares[i]}')

#-------------------------------------------------
for i in range(5):
  print('')
print('-'*10, 'Cuarto Ejercicio', '-'*10)

numbers = [21, 34, 17, 12, 29, 16, 10, 25]

odd_numbers = [number for number in numbers if number % 2 != 0]
print(odd_numbers)

#-------------------------------------------------
for i in range(5):
  print('')
print('-'*10, 'Quinto Ejercicio', '-'*10)

numbers = [35, 16, 10, 34, 37, 25]
even_numbers_v2 = [number for number in numbers if number % 2 == 0]
odd_numbers_v2 = [number for number in numbers if number % 2 != 0]

print(f'Numeros pares: \n {even_numbers_v2}')
print(f'Numeros Impares \n {odd_numbers_v2}')

#-------------------------------------------------
for i in range(5):
  print('')
print('-'*10, 'Primer Ejercicio', '-'*10)

words = ['python', 'programming', 'language', 'code', 'challenge']
word_lengths = {i: len(i) for i in words}

for item, valor in word_lengths.items():
  print(f'Palabra: {item} || Longitud: {valor}')


#-------------------------------------------------
for i in range(5):
  print('')
print('-'*10, 'Segundo Ejercicio', '-'*10)

text = 'Aprender Python es divertido y útil para el desarrollo.'

vowel_counts = {i: text.count(i) for i in text if i in 'aeiou'}
for item, valor in vowel_counts.items():
  print(f'Letra: {item} || Frecuencia: {valor}')

for i in range(5):
  print('')
print('-'*10, 'Tercer Ejercicio', '-'*10)

import random
random_numbers = [random.randint(1, 20) for _ in range(8)]

even_squared = {i: i**2 for i in random_numbers}

for item, valor in even_squared.items():
  print(f'Numero: {item} || Cuadrado: {valor}')

for i in range(5):
  print('')
print('-'*10, 'Cuarto Ejercicio', '-'*10)

celsius_temperatures = [20, 25, 30, 35, 10]

fahrenheit = {cel: (cel*9/5 + 32) for cel in celsius_temperatures}

for item, valor in fahrenheit.items():
  print(f'Celcius: {item} || Fahrenheit: {valor}')

for i in range(5):
  print('')
print('-'*10, 'Quinto Ejercicio', '-'*10)

divisible_by_three = [i for i in range(50) if i%3 == 0]

print('Los numeros entre 1 - 50 que son divisibles dentro de tres son los siguientes:')
for i in range(len(divisible_by_three)):
  if(i == len(divisible_by_three)-1):
    print(f'y {divisible_by_three[i]}.')
  elif i == len(divisible_by_three)-2:
    print(divisible_by_three[i], end=' ')
  else:
    print(divisible_by_three[i], end=', ')