import random
import collections
from collections import namedtuple
import math

PALOS = ['espada', 'basto', 'oro', 'copa']
VALORES = [1, 2, 3, 4, 5, 6, 7,8, 9, 10]

def crear_baraja():
	""" Una carta individual """
	barajas = []
	for palo in PALOS:
		for valor in VALORES:
			barajas.append((palo, valor))

	return barajas

def obtener_mano(barajas, tamano_mano):
	mano = random.sample(barajas, tamano_mano)

	return mano

def es_escalera(mano):
	mano_ordenada = []
	


def main(tamano_mano, intentos):
	barajas = crear_baraja()

	manos = []
	for _ in range(intentos):
		mano = obtener_mano(barajas, tamano_mano)
		manos.append(mano)

	escalera = 0
	for mano in manos:
		valores = []
		palos = []
		for carta in mano:
			valores.append(carta[1]) #son tuplas
			palos.append(carta[0])
		n = sum(valores) + len(valores)**2

		for pal in palos:
			if pal == palos[len(palos) - pal -1]:
				continue
		for val in valores:
			if val == len(valores) and n == True:
				escalera += 1


		

	probabilidad_corrida = escalera / intentos
	print(f' La probabilidad de obtener un par en una mano de {tamano_mano} barajas es de {probabilidad_corrida}')

if __name__ == '__main__':
	tamano_mano = int(input('Cuantas cartas por mano?: '))
	intentos = int(input('Cuantos intentos para calcular probabilidad: '))
	barajas = crear_baraja()
	
	main(tamano_mano, intentos)
	#print(barajas)

	#mano = obtener_mano(barajas, 5)

	#print(mano)