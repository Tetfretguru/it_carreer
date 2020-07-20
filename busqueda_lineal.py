import random #modulo para generar valores aleatorios

def busqueda_lineal(lista, objetivo):
	match = False

	for elemento in lista: #O(n)
		if elemento == objetivo:
			match = True
			break

	return match

def main():
	tamano_lista = int(input('De que tamaño será la lista: '))
	objetivo = int(input('Numero a encontrar: '))

	lista = [random.randint(0, 100) for i in range(tamano_lista)]

	encontrado = busqueda_lineal(lista, objetivo)
	print(lista)
	print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')


if __name__ == '__main__':
	main()