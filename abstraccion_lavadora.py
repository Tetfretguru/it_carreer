
class Lavadora:
	def __init__(self):
		pass

	def lavar(self, temperatura='frio'):
		"""Abstracción.
		Variables internas son funciones
		"""
		self._llenar_tanque(temperatura)
		self._anadir_jabon()
		self._lavar()
		self._centrifugar()

	def _llenar_tanque(self, temperatura):
		print(f'Lenando tanque con agua {temperatura}')

	def _anadir_jabon(self):
		print('Añadiendo jabon')

	def _lavar(self):
		print('Lavando...')

	def _centrifugar(self):
		print('Centrifugando la ropa...')

if __name__ == '__main__':
	lavadora = Lavadora()
	lavadora.lavar()