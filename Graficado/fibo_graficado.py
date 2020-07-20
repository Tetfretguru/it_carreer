from bokeh.plotting import figure, output_file, show
import sys


def fibonacci_recursivo(n):
	if n == 0 or n == 1:
		return 1

	return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

def fibonacci_dinamico(n, memo = {}):
	if n == 0 or n == 1:
		return 1

	try:
		return memo[n]
	except KeyError:
		resultado = fibonacci_dinamico(n - 1, memo) + fibonacci_dinamico(n - 2, memo)
		memo[n] = resultado

		return resultado

def main():
	sys.setrecursionlimit(10002) #cambia limite recursivo
	output_file('fibo_grafico.html')
	fig = figure()


	cantidad_vals = int(input('Cuantos valores quiere graficar: '))
	x_vals = list(range(cantidad_vals))
	y_vals = []

	for x in x_vals:
		val = int(input(f'Valor para calcular Suc.Fibonacci {x}: '))
		x_vals.append(val)
		if x == cantidad_vals - 1:
			break

	for n in x_vals:
		resultado = fibonacci_dinamico(n)
		y_vals.append(resultado)
	

	fig.line(x_vals, y_vals, line_width = 2)
	show(fig) 

if __name__ == '__main__':
	main()