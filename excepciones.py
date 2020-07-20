def divide_elementos_de_lista(lista, divisor):
	try:
		"""Al intentar ejecutar la función
		se agrega una excepción.
		Ésta es un mensaje de python, que al 
		añadirlo como expeción, no interrumpe
		ejecución.
		"""
		return [i / divisor for i in lista]
	except ZeroDivisionError as e:
		print(f'Error "{e}". No puede dividir entre cero.')
		return lista


lista = list(range(11))
divisor = 0

print(divide_elementos_de_lista(lista, divisor))