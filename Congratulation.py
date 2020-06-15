def congratulation():
  congratulation = input('Введите поздравление... ')
  cong = congratulation.upper()
  cong = list(cong)
  for i in cong:
      print('Скажите %s' % i)


congratulation()