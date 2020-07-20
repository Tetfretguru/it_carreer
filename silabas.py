palabra = input('Ingrese una palabra')
vocales = "aáeéiíoóuú"
consonantes = 'bcdfghjklmnñpqrstvwxyz'


indice = 0

while indice < len(palabra):
	for letra1 in palabra:
		for letra2 in vocales:
			for letra3 in consonantes:
				if letra1 == letra2 and indice == 0:
					print(letra1)
					if 
