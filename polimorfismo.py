
class Persona:
	def __init__(self, nombre):
		self.nombre = nombre

	def avanza(self):
		return 'Ando caminando'

class Ciclista(Persona):
	def __init__(self, nombre):
		super().__init__(nombre)

	def avanza(self):
		return 'Ando en bici'

class Motociclista(Persona):
	def __init__(self, nombre):
		super().__init__(nombre)

	def avanza(self):
		return 'Ando como bala wacho'

def main():
	persona = Persona('Tato')
	print(f'Soy {persona.nombre} y {persona.avanza()}')

	ciclista = Ciclista('Pepe')
	print(f'Soy {ciclista.nombre} y {ciclista.avanza()}')

	moto = Motociclista('Walter')
	print(f'{moto.avanza()}. El {moto.nombre} atr.')


if __name__ == '__main__':
	main()