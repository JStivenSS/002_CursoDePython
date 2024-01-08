def message_creator(text):
    # Escribe tu solución 👇
    respuestas = {
        'computadora': 'Con mi coputadora puedo programar usando python',
        'celular': 'En mi celular puedo aprender usando la app de Platzi',
        'cable': '¡Hay un cable en mi bota!'}
    if text in respuestas:
        return respuestas[text]
    else:
        return 'Artículo no encontrado'


text = 'cff'
response = message_creator(text)
print(response)
