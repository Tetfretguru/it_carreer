
def encuentra_vocales(word, vocales, cantidad):
	#vocales = "aáeéiíoóuú"
	#deletreo =[]
	
	#assert type(word) == str, f'{word} no es cadena.'
	#assert len(word) > 0, 'No se permite cadena vacía.'
	#deletreo.extend(word)

	
	indice = 0
	while indice < len(word):
		for letra in word:
			for letra2 in vocales:
				if letra == letra2:
					cont_vocal += 1
		indice += 1
		
	
	return cantidad 

	#print(f'La palabra {word} se deletra: ')
	#print(deletreo)
	


def main():
	word = input('Ingrese una palabra: ')
	vocales = 'aáeéiíoóuú'
	
	total = encuentra_vocales(word, vocales)
	print(f'Además posee {total} vocales.')


if __name__ == '__main__':
	main()