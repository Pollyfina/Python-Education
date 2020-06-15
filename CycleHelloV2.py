while True:
	whoiam = input('Кто ты?')
	if whoiam == 'стоп':
		print('До свидания')
		break
	elif whoiam == 'девочка':
		print('Доброе утро, солнышко!')
	elif whoiam == 'мальчик':
		print('Привет, парень.')
	else:
		print('Здравствуйте')