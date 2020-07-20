import operaciones as op 
cantidad = 0
op.lista_heroes = []
op.lista_nombre = []
while cantidad <= 1:
	nombre = input('Bienvenido a JLSysLog, ¿Cual es tu nombre?: ')  
	alter_ego = input('Oh, ya veo. ¿Cual es su identidad secreta: ')

	if nombre == 'Bruce Wayne' and alter_ego == 'Batman':
		print(f'Soy su fan. Bienvenido Sr. {nombre}.')
	elif nombre == 'Bruce Wayne' and alter_ego != 'Batman':
		print('Uted no es el Sr. Wayne.')
		break
	elif nombre != 'Bruce Wayne' and alter_ego == 'Batman':
		print('Usted no es Batman.')
		break
	else:
		welcome = (f'Bienvenido Sr/Sra {nombre} al JLSysLog. Aquí lo llamaremos {alter_ego}, para hacerlo mas facil.')
		print(f'{welcome} Por cierto ya gastamos {str(len(welcome))} caracteres hasta el primer enunciado.')
	
	op.lista_nombre.append(nombre)
	op.lista_heroes.append(alter_ego) 
	cantidad += 1	

op.check()	


#El código es hereditario, por lo que necesitamos importar toda una solución con objetos incluidos.	