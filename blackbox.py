import unittest #modulo de python que nos permite generar pruebas blackbox

def suma(num_1, num_2):
	return abs(num_1) + num_2 

class BlackBoxTest(unittest.TestCase):
	"""Test driver development"""
	def test_suma_dos_positivos(self):
		num_1 = 10
		num_2 = 5

		resultado = suma(num_1, num_2)

		self.assertEqual(resultado, 15) #asegurarnos que ese es el resultado
	def test_suma_dos_negativos(self):
		num_1 = -10
		num_2 = -7

		resultado = suma(num_1, num_2)

		self.assertEqual(resultado, -17)

if __name__ == '__main__': #el modulo actual como principal
	unittest.main() #en nuestro modulo principal
