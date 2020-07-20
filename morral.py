

def morral(tamano_morral, pesos, valores, n):
	
	if n == 0 or tamano_morral == 0:
		return 0

	if pesos[n - 1] > tamano_morral:
		print(f'Index {n-1} en valor {valores[n-1]} y peso {pesos[n-1]}. Exceso.')
		return morral(tamano_morral, pesos, valores, n-1)

	return max(valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n-1), morral(tamano_morral, pesos, valores, n - 1))








def main():
	valores = [60, 100, 120, 200, 240]
	pesos = [10, 20, 30, 40, 50]
	tamano_morral = int(input('Ingrese tamaño del morral: '))
	n = len(valores)

	resultado = morral(tamano_morral, pesos, valores, n)
	print(f'Este es el maximo: {resultado}')


if __name__ == '__main__':
	main()