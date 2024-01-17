asistentes = set()
asistentes_detalles = {}

def agregarAsistente(usuario):
  if usuario in asistentes:
    print('¡Este usuario ya se encuentra retistrado!')
  else:
    asistentes.add(usuario)
    print(f'{usuario} ha sido registrado de manera satisfactoria')

def agregarDetalles(usuairo, nombres, apellidos, edad, direccion, telefono):
  if usuairo in asistentes:
    print('El usuario no esta disponible')
  else:
    asistentes_detalles[usuairo] = {'nombres': nombres, 'apellidos': apellidos,'edad': edad, 'direccion':direccion, 'telefono': telefono}
    imprimir(usuairo)

def imprimir(usuario):
  print(asistentes_detalles[usuario]['nombres'])
i=1
usuario = ''
nombres = ''
apellidos = ''
edad = 0
direccion = ''
telefono = 0

while i != 0:
  print('si desea ingresar un usuario ingrese 1')
  print('si desea ingresar informacion a un usuario ingrese 2')
  i = int(input(f'pulse 0 para terminar el programa'))
  if i == 1:
    usuario = input('Ingrese el usuario que desea registrar')
    agregarAsistente(usuario)
  elif i == 2:
    usuario = input('Ingrese el usuario a ingresar detalles')
    if usuario in asistentes:
      nombres = input('ingrese el nombre')
      apellidos = input('ingrese el apellido')
      edad = int(input('ingrese numero de telefono'))
      direccion = input('ingrese la direccion del asistente')
      telefono = int(input('ingrese el nombre'))
      agregarDetalles(usuario, nombres, apellidos, edad, direccion, telefono)
    else:
      print('El usuario no esta registrado')
  elif i == 0:
    print('Gracias por usar el sistema')
  else:
    print('escoja una opcion valida')