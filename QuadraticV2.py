from math import sqrt

def quadratic():
	a = input('Введите а')
	b = input('Введите b')
	c = input('Введите с')
	a = int(a)
	b = int(b)
	c = int(c)
	if a == 0 and b == 0 and c == 0:
		print('Это не уранение')
	elif a == 0 and b == 0:
		x = -c
		print('Корней нет')
	elif a == 0:
		x = -c/b
		print(x)
	else:
		D = b**2-4*a*c
		if D < 0:
			print('Корней нет')
		elif D == 0:
			x = -b/(2*a)
			print('x = %s' % x)
		else:
			D = b**2-4*a*c
			d = sqrt(D) 
			x1 = (-b+d)/(2*a)
			x2 = (-b-d)/(2*a)
			print('x1 = %s' % x1)
			print('x2 = %s' % x2)