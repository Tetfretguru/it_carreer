def factorial(n):
	"""Calcula el factorial de n.

	n int > 0
	returns n!
	"""
	print(n)
	if n == 1:
		return 1

	return n * factorial(n - 1)
		"""Al ejecutarse a sí misma entre en un loop (recursividad) """
n = int(input('Escribe un entero: '))

print(factorial(n))
