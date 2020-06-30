'''
This is the first doctest.
>>> inequalities(1,1,1)
Уравнение < 0 если x ∈ Ø
Уравнение > 0 если x ∈ ℝ
>>> inequalities(1,-10,24)
Уравнение < 0 если x ∈ (4.0;6.0)
Уравнение = 0 если x = 4.0 или x = 6.0
Уравнение > 0 если x ∈ (-∞;4.0)U(6.0;+∞)
>>> inequalities(-3,-4,7)
Уравнение < 0 если x ∈ (-∞;-2.3333333333333335)U(1.0;+∞)
Уравнение = 0 если x = -2.3333333333333335 или x = 1.0
Уравнение > 0 если x ∈ (-2.3333333333333335;1.0)
>>> inequalities(0,0,0)
Это не уравнение
'''


from math import sqrt


def inequalities(a,b,c):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
    except ValueError:
        print('Вы ввели не число')
    else:
        if a == 0 and b == 0 and c == 0:
            print('Это не уравнение')
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
        else:#здесь программа начинает считать именно неравенство
            D = b**2-4*a*c
            if D > 0:
                d = sqrt(D)
                x1 = (-b-d)/(2*a)
                x2 = (-b+d)/(2*a)
                if x1 > x2:
                    x1 = (-b+d)/(2*a)
                    x2 = (-b-d)/(2*a)
                    if a > 0:
                        print('Уравнение < 0 если x ∈ ({0};{1})'.format(x1,x2))
                        print('Уравнение = 0 если x = {0} или x = {1}'.format(x1, x2))
                        print('Уравнение > 0 если x ∈ (-∞;{0})U({1};+∞)'.format(x1, x2))
                    elif a < 0:
                        print('Уравнение < 0 если x ∈ (-∞;{0})U({1};+∞)'.format(x1, x2))
                        print('Уравнение = 0 если x = {0} или x = {1}'.format(x1, x2))
                        print('Уравнение > 0 если x ∈ ({0};{1})'.format(x1,x2))
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


if __name__ == "__main__":
    import doctest
    doctest.testmod()