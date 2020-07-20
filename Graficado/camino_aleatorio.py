
from borracho import BorrachoTradicional
from campo import Campo
from coordenadas import Coordenada
from bokeh.plotting import figure, show, output_file

def caminata(campo, borracho, pasos):
	"""Interactuamos con las clase Campo, mayormente"""
	inicio = campo.obtener_coordenada(borracho) #Devuelve un array 

	for _ in range(pasos):
		campo.mover_borracho(borracho) #metodo en Campo, heredado de Borracho

	return inicio.distancia(campo.obtener_coordenada(borracho)) #regresa un array, [for i in inicio] == al teorema de Pitagoras en el metodo distancia() en Coordenada


def simular_caminata(pasos, numero_de_intentos, tipo_de_boracho):
	borracho = tipo_de_boracho(nombre = 'Tato') #funcion agnostica
	""" Llama a BorrachoTradicional, asignandole un nombre al metodo __init__ constructor"""
	origen = Coordenada(0, 0) #Genera una instancia con el metodo mover() de la clase Coordenada
	distancias = []

	for _ in range(numero_de_intentos):
		campo = Campo() #Instancia de la clase
		campo.anadir_borracho(borracho, origen) #metodo de la clase Campo
		simulacion_caminata = caminata(campo, borracho, pasos) #asignamos de un return de la funcion
		distancias.append(round(simulacion_caminata, 1))
	return distancias

def graficar(x, y):
	"""Por default genera un archivo html """
	output_file('Borracho grafica.html')
	grafica = figure(title = 'Camino borracho', x_axis_label = 'Pasos', y_axis_label = 'Distancia recorrida')
	grafica.line(x, y, line_width = 3)

	show(grafica)




def main(distancias_de_caminata, numero_de_intentos, tipo_de_boracho):
	distancias_m_por_caminata = []
	distancias_maximas = []
	distancias_minimas = []

	#array = [distancias_m_por_caminata, distancia_maxima, distancias_minimas]

	for pasos in distancias_de_caminata:
		distancias = simular_caminata(pasos, numero_de_intentos, tipo_de_boracho)
		
		distancia_media = round(sum(distancias) / len(distancias), 4) #4 son las posibles direcciones
		distancia_maxima = max(distancias)
		distancia_minima = min(distancias)

		distancias_maximas.append(distancia_maxima)
		distancias_minimas.append(distancia_minima)
		distancias_m_por_caminata.append(distancia_media)


		
		print(f'{tipo_de_boracho.nombre} caminata aleatoria de {pasos}')
		print(f'Media = {distancia_media}')
		print(f'Max = {distancia_maxima}')
		print(f'Minima = {distancia_minima}')

	graficar(distancias_de_caminata, distancias_minimas)
	



"""Entry point """
if __name__ == '__main__':
	distancias_de_caminata = [10, 100, 1000, 10000]
	numero_de_intentos = 100

	main(distancias_de_caminata, numero_de_intentos, BorrachoTradicional)