asistentes = set()
asistentes_detalles = {}

def agregarAsistente(usuario):
  asistentes.add(usuario)
  print(f'{usuario} ha sido registrado de manera satisfactoria')

def agregarDetalles(usuairo, nombres, apellidos, edad, direccion, telefono):
  asistentes_detalles[usuairo] = {'nombres': nombres, 'apellidos': apellidos,'edad': edad, 'direccion':direccion, 'telefono': telefono}
  imprimir(usuairo)

def imprimir(usuario):
  print(asistentes_detalles[usuario]['nombres'])

agregarAsistente('JStivenSS')
agregarDetalles('JStivenSS', 'Stiven', 'Sirin', 17, 'Santa Cruz Balanyá, Chimaltenango', 45241475)