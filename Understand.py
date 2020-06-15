def understand(phrase):
    #phrase = input('Введите фразу ')
    phrase = phrase.strip().lower()
    if phrase == 'да' or phrase == 'хочу' or phrase == 'почему бы и нет':
        return True
    elif phrase == 'нет' or phrase == 'не хочу':
        return False
    else:
        phrase.split(' ')
        try:
            phrase.index('нет')
        except ValueError:
            try:
                phrase.index('не')
            except ValueError:
                return True
            else:
                return False
        else:
            return False