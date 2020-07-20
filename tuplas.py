my_tuple = (1, )


my_otupule = (2, 4, 4)

my_tuple += my_otupule

x, y, z = my_otupule #se asignan esas letras en representatividad de cada valor de la tupla

def coordenadas():
	""" Regresa dos valores

	posteriormente, se asignan a una nueva tupla nueva: coordenada

	"""
	return (5, 4)

coordenada = coordenadas()
coordenada

x, y = coordenadas()
print(x, y)
