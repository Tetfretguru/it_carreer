#objetivo = int(input('Escoge un numero: '))
def aprox():
	epsilon = 0.01 #que tan cerca queremos llegar de la respuesta
	paso = epsilon**2. #qué tanto nos estamos acercando en cada iteración a la respuesta
	respuesta = 0.0 

	while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
		print(abs(respuesta**2 - objetivo), respuesta)
		respuesta += paso

	if abs(respuesta**2 - objetivo) >= epsilon:
		print(f'No se encontró la raíz cuadrada de {objetivo}')
	else:
		print(f'La raíz cuadrada de {objetivo} es {respuesta}')
