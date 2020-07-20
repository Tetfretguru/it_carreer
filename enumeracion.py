#objetivo = int(input('Ingrese un número entero: '))
def enumerar():
	respuesta = 0 #0**0 = 1, y es el primer entero
	while respuesta**2 < objetivo:
		print(respuesta) #enumera posibilidades, es decir, va probando uno a uno pero a velocidades inimaginables
		respuesta += 1

	if respuesta**2 == objetivo:
		print(f'La raíz cuadrada de {objetivo} es {respuesta}')
	else:
		print(f'{objetivo} no tiene una raíz cuadrada entera.')	
		
