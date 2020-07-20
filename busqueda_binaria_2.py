import random #modulo para generar valores aleatorios

def busqueda_binaria(lista, comienzo, final, objetivo):
	print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
	if comienzo > final:
		return False

	medio = (comienzo + final) // 2 #division enteros

	if lista[medio] == objetivo:
		return True
	elif lista[medio] < objetivo:
		return busqueda_binaria(lista, medio + 1, final, objetivo)
	else:
		return busqueda_binaria(lista, comienzo, medio - 1, objetivo)	

	

def main():
	tamano_lista = int(input('De que tamaño será la lista: '))
	objetivo = int(input('Numero a encontrar: '))

	lista = sorted([random.randint(0, 100) for i in range(tamano_lista)]) #ordena

	encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
	print(lista)
	print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')


if __name__ == '__main__':
	main()