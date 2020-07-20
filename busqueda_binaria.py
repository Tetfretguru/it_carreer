#objetivo = int(input('Escoge un numero: '))
def binbusq():
	epsilon = 0.001
	bajo = 0.0 #divisor que es == 1
	alto = max(1.0, objetivo) #devuelve el maximo entre 1 (entero mas pequeño) y el nro del usuario
	respuesta = (alto + bajo) / 2 #achica las posibilidades a la mitad por sentencia

	while abs(respuesta**2 - objetivo) >= epsilon:
		print(f'bajo = {bajo}, alto = {alto}, respuesta = {respuesta}')  #nos funciona de monitor para ver el contenido de las variables en cada iteración
		if respuesta**2 < objetivo:      #si es menor, pasa a ser bajo
			bajo = respuesta
		else:
			alto = respuesta			#si es mayor, pasa a ser alto

		respuesta = (alto + bajo) / 2

	print(f'La raíz cuadrada de {objetivo} es {respuesta}')