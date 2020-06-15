def func2():
    file = open('Desktop/Test_file.txt', 'r')
    number_of_symbols = 0
    for line in file:
       add = len(line)
       print(add)
       number_of_symbols = number_of_symbols + add
    print(number_of_symbols)


func2()