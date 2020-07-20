contador_externo = 0
contador_interno = 0

while contador_externo <= 24:
	while contador_interno < 60:
		print(f'{str(contador_externo)}hh:{str(contador_interno)}mm')
		contador_interno += 1
		if contador_interno == 60:
			break
	contador_externo += 1
	contador_interno = 0
	if contador_externo == 24:
		break

print('Se ha cumplido un día.')

		

#"relojes dentro de relojes"