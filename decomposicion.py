
class Automovil: #super class
	def __init__(self, modelo, marca, color):
		self.modelo = modelo
		self.marca = marca
		self.color = color
		self._estado = 'en reposo' #variables privadas con "_variable"
		self._motor = None

	def __repr__(self):
		"""Para muchos tipos, esta función intenta devolver una cadena que produciría un objeto con el mismo valor cuando se pasa a eval(); 
		de lo contrario, la representación es una cadena encerrada entre paréntesis angulares 
		que contiene el nombre del tipo de objeto junto con Información que a menudo incluye el nombre
		y la dirección del objeto. 
		Una clase puede controlar lo que esta función devuelve para sus instancias definiendo un método __repr__().
		"""
		return f'Automovil de caracteristicas Modelo: {self.modelo} / Marca: {self.marca} / Color: {self.color}'

	def acelerar(self, tipo='rapida'):
		self.tipo = tipo
		
		if tipo == 'despacio':
			self.Motor.inyecta_nafta(self, 10)
			print('Va rapido, bobo.')
		else:
			self.Motor.inyecta_nafta(self, 3)
			print('Lento pero seguro.')
		
		self._estado = 'en movimiento'
		print(f'Automovil {self._estado}.')
		print(' ')


	class Motor:
		def __init__(self, cilindros, tipo='nafta'):
			self.cilindros = cilindros
			self.tipo = tipo	
			self._temperatura = 0

		def __repr__(self):
			return f'de {self.cilindros} cilindros, tipo {self.tipo}'

		def inyecta_nafta(self, cantidad):
			self.cantidad = cantidad

			return cantidad
		

if __name__ == '__main__':
	Automovil_1 = Automovil('Uno', 'Fiat', 'Verde')
	Automovil_1.acelerar()
	Motor_1 = Automovil.Motor(4, 'Nafta')
	Automovil_2 = Automovil('Aveo', 'Chevrolet', 'Blanco')
	Automovil_2.acelerar()
	Motor_2 = Automovil.Motor(4, 'Nafta')


print(f'{repr(Automovil_1)} y motor {repr(Motor_1)}')
print(f'{repr(Automovil_2)} y motor {repr(Motor_2)}')



	