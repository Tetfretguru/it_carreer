import enumeracion as en
import busqueda_binaria as binbus
import aproximacion as aprox
objetive = int(input('Ingrese un número entero: '))

print("Escoja una de las siguientes opciones...")
opcion = int(input('1- EE  2- BB  3-Aprox.  :'))

while opcion != 4:
	if opcion == 1:
		en.objetivo = objetive
		en.enumerar()
		break
	elif opcion == 2:
		binbus.objetivo = objetive
		binbus.binbusq()
		break
	elif opcion == 3:
		aprox.objetivo = objetive
		aprox.aprox()
		break
	else:
		print(f'{opcion} no es una opcion.')
		



