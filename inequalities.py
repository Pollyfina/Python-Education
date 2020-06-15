from math import sqrt
from Understand import understand

#∈ - знак принадлежности
#∞ - знак бесконечности
#∪ - знак объединения
#Ø - знак пустого множества
#ℝ - множество рациональных чисел

def inequalities():
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
            if c < 0:
                print('Уравнение < 0 если x ∈ ℝ')
            else:
                print('Уравнение > 0 если x ∈ ℝ')
        elif a == 0 and b != 0 and c != 0:
            x = -c/b
            if b > 0:
                print('Уравнение < 0 если x ∈ (-∞;%s)' % x)
                print('Уравнение = 0 если x = %s' % x)
                print('Уравнение > 0 если x ∈ (%s;+∞)' % x)
            else:
                print('Уравнение < 0 если x ∈ (%s;+∞)' % x)
                print('Уравнение = 0 если x = %s' % x)
                print('Уравнение > 0 если x ∈ (-∞;%s)' % x)
        elif b == 0 and a != 0 and c != 0:
            D = b**2-4*a*c
            if D > 0:
                d = sqrt(D)
                x1 = (-b-d)/(2*a)
                x2 = (-b+d)/(2*a)
                if x1 > x2:
                    x1 = (-b+d)/(2*a)
                    x2 = (-b-d)/(2*a)
                else:
                    if a > 0:
                        print('Уравнение < 0 если x ∈ ({0};{1})'.format(x1,x2))
                        print('Уравнение = 0 если x = {0} или x = {1}'.format(x1, x2))
                        print('Уравнение > 0 если x ∈ (-∞;{0})U({1};+∞)'.format(x1, x2))
                    elif a < 0:
                        print('Уравнение < 0 если x ∈ (-∞;{0})U({1};+∞)'.format(x1, x2))
                        print('Уравнение = 0 если x = {0} или x = {1}'.format(x1, x2))
                        print('Уравнение > 0 если x ∈ ({0};{1})'.format(x1,x2))
            elif D == 0:
                d = sqrt(D)
                x1 = (-b-d)/(2*a)
                x2 = (-b+d)/(2*a)
                if a > 0:
                    print('Уравнение < 0 если x ∈ Ø')
                    print('Уравнение = 0 если x = {0}'.format(x1))
                    print('Уравнение > 0 если x ∈ ℝ \ [{0}]'.format(x1))
                elif a < 0:
                    print('Уравнение < 0 если x ∈ ℝ \ [{0}]'.format(x1))
                    print('Уравнение = 0 если x = {0}'.format(x1))
                    print('Уравнение > 0 если x ∈ Ø')
            else:
                if a > 0:
                    print('Уравнение < 0 если x ∈ Ø')
                    print('Уравнение > 0 если x ∈ ℝ')
                elif a < 0:
                    print('Уравнение < 0 если x ∈ ℝ')
                    print('Уравнение > 0 если x ∈ Ø')
        elif c == 0 and a != 0 and b != 0:
            D = b**2-4*a*c
            if D < 0:
                print('Что-то пошло не так')
            elif D == 0:
                d = sqrt(D)
                x1 = (-b-d)/(2*a)
                x2 = (-b+d)/(2*a)
                if a > 0:
                    print('Уравнение < 0 если x ∈ Ø')
                    print('Уравнение = 0 если x = {0}'.format(x1))
                    print('Уравнение > 0 если x ∈ ℝ \ [{0}]'.format(x1))
                elif a < 0:
                    print('Уравнение < 0 если x ∈ ℝ \ [{0}]'.format(x1))
                    print('Уравнение = 0 если x = {0}'.format(x1))
                    print('Уравнение > 0 если x ∈ Ø')
            else:
                if a > 0:
                    print('Уравнение < 0 если x ∈ Ø')
                    print('Уравнение > 0 если x ∈ ℝ')
                elif a < 0:
                    print('Уравнение < 0 если x ∈ ℝ')
                    print('Уравнение > 0 если x ∈ Ø')
        else:
            D = b**2-4*a*c
            if D > 0:
                d = sqrt(D)
                x1 = (-b-d)/(2*a)
                x2 = (-b+d)/(2*a)
                if x1 > x2:
                    x1 = (-b+d)/(2*a)
                    x2 = (-b-d)/(2*a)
                else:
                    if a > 0:
                        print('Уравнение < 0 если x ∈ ({0};{1})'.format(x1,x2))
                        print('Уравнение = 0 если x = {0} или x = {1}'.format(x1, x2))
                        print('Уравнение > 0 если x ∈ (-∞;{0})U({1};+∞)'.format(x1, x2))
                    elif a < 0:
                        print('Уравнение < 0 если x ∈ (-∞;{0})U({1};+∞)'.format(x1, x2))
                        print('Уравнение = 0 если x = {0} или x = {1}'.format(x1, x2))
                        print('Уравнение > 0 если x ∈ ({0};{1})'.format(x1,x2))
            elif D == 0:
                d = sqrt(D)
                x1 = (-b-d)/(2*a)
                x2 = (-b+d)/(2*a)
                if a > 0:
                    print('Уравнение < 0 если x ∈ Ø')
                    print('Уравнение = 0 если x = {0}'.format(x1))
                    print('Уравнение > 0 если x ∈ ℝ \ [{0}]'.format(x1))
                elif a < 0:
                    print('Уравнение < 0 если x ∈ ℝ \ [{0}]'.format(x1))
                    print('Уравнение = 0 если x = {0}'.format(x1))
                    print('Уравнение > 0 если x ∈ Ø')
            else:
                if a > 0:
                    print('Уравнение < 0 если x ∈ Ø')
                    print('Уравнение > 0 если x ∈ ℝ')
                elif a < 0:
                    print('Уравнение < 0 если x ∈ ℝ')
                    print('Уравнение > 0 если x ∈ Ø')


while True:
    phrase = input('Хотите ли вы решать квадратные неравенства? ')
    want = understand(phrase)
    if want:
        inequalities()
    else:
        break