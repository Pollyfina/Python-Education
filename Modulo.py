def modulo():
    a = input('Введите число 1 ')
    b = input('Введите число 2 ')
    a.strip()
    b.strip()
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        print('Человечество ещё не умеет делить буквы...')
    else:
        try:
            a%b
        except ZeroDivisionError:
            print('Делить на ноль вредно для здоровья')
        else:
            print('Остаток от целочисленного деления = {}'.format(a%b))


modulo()