def whereigo():
	age = input('Сколько вам лет?')
	age.strip()
	age = int(age)
	if age >= 0 and age <= 5:
		print('Детский садик')
	elif age >= 6 and age <= 17:
		print('Школа')
	elif age >= 18 and age < 23:
		print('Институт')
	elif age >= 23:
		print('Работа')
	else:
		print('Вы ещё не родились')