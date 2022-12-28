# Расставьте знаки + между некоторыми цифрами числа 12345678910111213...N, чтобы в сумме получилось число M.
# На вход получаем два натуральных числа N и M.
# Вывод: верные примеры в строку.
# Примеры:
# 1)Ввод: 5 15
# Вывод: 1+2+3+4+5=15
# 2)Ввод: 4 46
# Вывод: 12+34=46


def function(quantity, result):
    if quantity <= 0:
        return 'N должно быть натуральным.'
    elif result <= 0:
        return 'M должно быть натуральным.'
    elif quantity == 1:
        return 'У вас должно быть, как минимум, 2 цифры для осуществления суммы.'
    elif quantity in range(2, 5+1):
        sample = ''
        numbers_str = [str(i) for i in range(quantity + 1)][1::]
        if quantity == 2:
            for index in range(len(numbers_str)):
                if index != len(numbers_str) - 1:
                    numbers_str[index] += '+'
                sample += numbers_str[index]
            if eval(sample) == result:
                return sample + '=' + str(result)
            return 'Не найдено сопоставление примера из цирф N и результата M.'
        elif quantity == 3:
            for index in range(len(numbers_str)):
                if index != len(numbers_str) - 1:
                    numbers_str[index] += '+'
                sample += numbers_str[index]
            if eval(sample) == result:
                return sample + '=' + str(result)
            else:
                sample = ''
                numbers_str = [str(i) for i in range(quantity + 1)][1::]
                for index in range(len(numbers_str)):
                    if index != len(numbers_str) - 1:
                        variable = numbers_str[index]
                        numbers_str[index] += '+'
                        for under_index in range(len(numbers_str)):
                            sample += numbers_str[under_index]
                        if eval(sample) == result:
                            return sample + '=' + str(result)
                        else:
                            sample = ''
                            numbers_str[index] = variable
                return 'Не найдено сопоставление примера из цирф N и результата M.'
        elif quantity == 4:
            for index in range(len(numbers_str)):
                if index != len(numbers_str) - 1:
                    numbers_str[index] += '+'
                sample += numbers_str[index]
            if eval(sample) == result:
                return sample + '=' + str(result)
            else:
                sample = ''
                numbers_str = [str(i) for i in range(quantity + 1)][1::]
                for index in range(len(numbers_str)):
                    if index != len(numbers_str) - 1:
                        variable = numbers_str[index]
                        numbers_str[index] += '+'
                        for under_index in range(len(numbers_str)):
                            sample += numbers_str[under_index]
                        if eval(sample) == result:
                            return sample + '=' + str(result)
                        else:
                            sample = ''
                            for under_index in range(len(numbers_str)):
                                if under_index != len(numbers_str) - 1 and under_index != index:
                                    variable_2 = numbers_str[under_index]
                                    numbers_str[under_index] += '+'
                                    for under_under_index in range(len(numbers_str)):
                                        sample += numbers_str[under_under_index]
                                    if eval(sample) == result:
                                        return sample + '=' + str(result)
                                    else:
                                        sample = ''
                                        numbers_str[under_index] = variable_2
                            numbers_str[index] = variable

                return 'Не найдено сопоставление примера из цирф N и результата M.'

        elif quantity == 5:
            for index in range(len(numbers_str)):
                if index != len(numbers_str) - 1:
                    numbers_str[index] += '+'
                sample += numbers_str[index]
            if eval(sample) == result:
                return sample + '=' + str(result)
            else:
                sample = ''
                numbers_str = [str(i) for i in range(quantity + 1)][1::]
                for index in range(len(numbers_str)):
                    if index != len(numbers_str) - 1:
                        variable = numbers_str[index]
                        numbers_str[index] += '+'
                        for under_index in range(len(numbers_str)):
                            sample += numbers_str[under_index]
                        if eval(sample) == result:
                            return sample + '=' + str(result)
                        else:
                            sample = ''
                            for under_index in range(len(numbers_str)):
                                if under_index != len(numbers_str) - 1 and under_index != index:
                                    variable_2 = numbers_str[under_index]
                                    numbers_str[under_index] += '+'
                                    for under_under_index in range(len(numbers_str)):
                                        sample += numbers_str[under_under_index]
                                    if eval(sample) == result:
                                        return sample + '=' + str(result)
                                    else:
                                        sample = ''
                                        for under_under_index in range(len(numbers_str)):
                                            if under_under_index != len(numbers_str) - 1 and under_under_index != index:
                                                variable_3 = numbers_str[under_under_index]
                                                numbers_str[under_under_index] += '+'
                                                for under_under_under_index in range(len(numbers_str)):
                                                    sample += numbers_str[under_under_under_index]
                                                if eval(sample) == result:
                                                    return sample + '=' + str(result)
                                                else:
                                                    sample = ''
                                                    numbers_str[under_under_index] = variable_3
                                        numbers_str[under_index] = variable_2
                            numbers_str[index] = variable
    else:
        return 'N чересчур большое.'

# quantity, result = map(int, input('N, M: ')
# print(function(quantity, result))


def test():
    assert function(-1, 3) == 'N должно быть натуральным.', 'Error1'
    assert function(4, -1) == 'M должно быть натуральным.', 'Error2'
    assert function(1, 5) == 'У вас должно быть, как минимум, 2 цифры для осуществления суммы.', 'Error3'
    assert function(-1, -1) == 'N должно быть натуральным.', 'Error4'
    assert function(2, 3) == '1+2=3', 'Error5'
    assert function(3, 6) == '1+2+3=6', 'Error6'
    assert function(3, 15) == '12+3=15', 'Error7'
    assert function(3, 24) == '1+23=24', 'Error8'
    assert function(3, 24) == '1+23=24', 'Error9'
    assert function(4, 10) == '1+2+3+4=10', 'Error10'
    assert function(4, 19) == '12+3+4=19', 'Error11'
    assert function(4, 28) == '1+23+4=28', 'Error12'
    assert function(4, 37) == '1+2+34=37', 'Error13'
    assert function(4, 235) == '1+234=235', 'Error14'
    assert function(4, 46) == '12+34=46', 'Error15'
    assert function(4, 127) == '123+4=127', 'Error16'
    assert function(5, 15) == '1+2+3+4+5=15', 'Error17'
    assert function(5, 2346) == '1+2345=2346', 'Error18'
    assert function(5, 357) == '12+345=357', 'Error19'
    assert function(5, 168) == '123+45=168', 'Error20'
    assert function(5, 1239) == '1234+5=1239', 'Error21'
    assert function(5, 348) == '1+2+345=348', 'Error22'
    assert function(5, 69) == '1+23+45=69', 'Error23'
    assert function(5, 240) == '1+234+5=240', 'Error24'
    assert function(5, 60) == '12+3+45=60', 'Error25'
    assert function(5, 132) == '123+4+5=132', 'Error26'
    assert function(5, 33) == '1+23+4+5=33', 'Error27'
    assert function(5, 24) == '12+3+4+5=24', 'Error28'
    assert function(5, 42) == '1+2+34+5=42', 'Error29'
    assert function(6, 20) == 'N чересчур большое.', 'Error30'
    assert function(30, 20) == 'N чересчур большое.', 'Error31'

test()
