import random #modulo para generar valores aleatorios

def ordenamiento_por_mezcla(lista):
	if len(lista) > 1:
		medio = len(lista) // 2
		izquierda = lista[:medio]
		derecha = lista[medio:]
		print(f'izquierda {izquierda}', '*' * 5, f'derecha {derecha}')

		#llamada recursiva en cada mitad
		ordenamiento_por_mezcla(izquierda)
		ordenamiento_por_mezcla(derecha)

		#iteradores para recorrer las dos sublistas
		i = 0
		j = 0
		#iterador para lista principal
		k = 0

		while i < len(izquierda) and j < len(derecha):
			if izquierda[i] < derecha[j]:
				lista[k] = izquierda[i]
				i += 1
			else:
				lista[k] = derecha[j]
				j += 1

			k += 1

			#lo añade a la lista
		while i < len(izquierda):
			lista[k] = izquierda[i]
			i += 1
			k += 1

		while j < len(derecha):
			lista[k] = derecha[j]
			j += 1
			k += 1
		print(f'comparando: izquierda {izquierda}, derecha{derecha}')
		print(f'lista final {lista}')
		print('-' * 50)
		""" EJECUTA TODO DE IIZQ A DER y al reves"""
	return lista
	 
	

def main():
	tamano_lista = int(input('De que tamaño será la lista: '))
	

	lista = [random.randint(0, 100) for i in range(tamano_lista)]
	print(lista) 
	print('-' * 20)

	lista_ordenada = ordenamiento_por_mezcla(lista)
	print(f'Lista ordenada {lista_ordenada}')


if __name__ == '__main__':
	main()