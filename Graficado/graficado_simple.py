from bokeh.plotting import figure, output_file, show
#desde la librería, las funciones de graficado (figura), para generar un output y para mostrar

def main():
	output_file('graficado_simple.html')
	fig = figure()

	total_vals = int(input('Cuantos valores quieres graficar?: '))
	x_vals = list(range(total_vals))
	y_vals = []

	for x in x_vals:
		val = int(input(f'Valor Y para {x} '))
		y_vals.append(val)

	fig.line(x_vals, y_vals, line_width = 2)
	show(fig)

if __name__ == '__main__':
	main()

