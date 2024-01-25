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
  numero = max(numeros)
  return numero

max_number = find_max(numbers)
print(f'El número máximo en la lista es: {max_number}')

#----------------------------------------------------------------  
for i in range(5):
  print('')
print('-'*10,'Cuarto Ejercicio','-'*10)

def is_prime(numero):
  iteraciones = 0
  valor = { numero: True}
  for i in range(numero):
    if numero % (i+1) == 0:
      iteraciones += 1

  if(iteraciones > 2):
    valor[numero: False]
  return valor

result = is_prime(99)
for item, valor in result.items():
  print(f'¿{item} es primo? {valor}')

#----------------------------------------------------------------  
for i in range(5):
  print('')
print('-'*10,'Quinto Ejercicio','-'*10)

def reverse_string(texto):
  text = texto[::-1]
  return text
original_string = 'Python'
reversed_string = reverse_string(original_string)
print(f'Cadena original: {original_string}\nCadena invertida: {reversed_string}')