import random
from estadisticas import media, varianza, desviacion_std

def tirar_dado(numero_de_tiros):
	secuencia_de_tiros = []
	

	for _ in range(numero_de_tiros):
		tiro = random.choice([1, 2, 3, 4, 5, 6]) #Dado 1
		tiro_2 = random.choice([1, 2, 3, 4, 5, 6]) #Dado 2
		secuencia_de_tiros.append(tiro + tiro_2)
	return secuencia_de_tiros


def main(numero_de_tiros, numero_de_intentos):
	tiros = []
	
	for _ in range(numero_de_intentos):
		secuencia_de_tiros = tirar_dado(numero_de_tiros)
		tiros.append(secuencia_de_tiros)
		
		

	#tiros_con_1 = 0
	tiros_con_12 = 0
	
	for tiro in tiros:
		if 12 not in tiro:
				tiros_con_12 += 1


	#probabilidad_tiros_c_1 = tiros_con_1  / numero_de_intentos
	probabilidad_tiros_c_12 = tiros_con_12 / numero_de_intentos
	
	#print(f'Probabilidad de no obtener por lo menos un 1 en {numero_de_tiros} tiros = {probabilidad_tiros_c_1}')
	print(f'Probabilidad de obtener por lo menos un 12 en {numero_de_tiros} tiros = {probabilidad_tiros_c_12}')

if __name__ == '__main__':
	numero_de_tiros = int(input('Cuantos tiros de dado: '))
	numero_de_intentos = int(input('Cuantas veces correrá simulacion: '))

	main(numero_de_tiros, numero_de_intentos)