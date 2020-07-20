class CassillaDeVoto:
	def __init__(self, identificador,	pais):
		self._identificador = identificador
		self._pais = pais
		self._region = None

	@property
	def region(self):
		return self._region

	@region.setter
	def set_region(self, region):
		if region in self._pais: #se puede buscar una vez utilizando "in"
			self._region = region

		raise ValueError(f'La region {region} no es válida en {self.pais}')


casilla = CassillaDeVoto(123, ['Montevideo', 'Florida', 'Durazno'])
casilla.region(region)
print(casilla.region)
"""casilla.region = 'Florida'
casilla.region"""