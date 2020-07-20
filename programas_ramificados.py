persona_1 = input('Hola, ¿cómo te llamas?: ')
edad_persona_1 = int(input('¿Cuántos años tienes?: '))
persona_2 = input('Tu, ¿cómo te llamas?: ')
edad_persona_2 = int(input('¿Cuántos años tienes?: '))

if persona_1 != persona_2 and edad_persona_1 != edad_persona_2:
	if edad_persona_1 > edad_persona_2:
		print(f'{persona_1} es mayor que {persona_2}')
	elif edad_persona_1 < edad_persona_2:
		print(f'{persona_2} es mayor que {persona_1}')
	else:
		print('Tienen la misma edad')
else:
	print('Son la misma persona')	