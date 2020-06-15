from math import sqrt

def quadratic():
    a = input('Введите а ')
    b = input('Введите b ')
    c = input('Введите с ')
    a.strip()
    b.strip()
    c.strip()
    try:
      a = int(a)
      b = int(b)
      c = int(c)
    except ValueError:
        print('Вы ввели не число')
    else:
        if a == 0 and b == 0 and c == 0:
            print('Это не уранение')
        elif a == 0 and b == 0 and c != 0:
            print('Корней нет')
        elif a == 0 and b != 0 and c != 0:
            x = -c/b
            print(x)
        elif b == 0 and a != 0 and c != 0:
            if a < 0 and c > 0:
                x = -c/a
                x1 = sqrt(x)
                x2 = x1/-1
                print('x1 = %s' % x1)
                print('x2 = %s' % x2)
            elif a > 0 and c < 0:
                x = -c/a
                x1 = sqrt(x)
                x2 = x1/-1
                print('x1 = %s' % x1)
                print('x2 = %s' % x2)
            else:
                print('Корней нет')
        elif c == 0 and a != 0 and b != 0:
            x1 = 0
            x2 = -c
            print('x1 = %s' % x1)
            print('x2 = %s' % x2)
        else:
            D = b**2-4*a*c
            if D < 0:
                print('D = %s' % D)
                print('Корней нет')
            elif D == 0:
                x = -b/(2*a)
                print('D = %s' % D)
                print('x = %s' % x)
            else:
                D = b**2-4*a*c
                d = sqrt(D) 
                x1 = (-b+d)/(2*a)
                x2 = (-b-d)/(2*a)
                print('D = %s' % D)
                print('x1 = %s' % x1)
                print('x2 = %s' % x2)


while True:
    want = input('Хотите ли вы решать квадратные уравнения? ')
    want = want.lower()
    want = want.strip()
    if want == 'да' or want == 'хочу':
        quadratic()
    elif want == 'нет' or want == 'не хочу':
        break
    else:
        print('Я вас не понимаю :-(')