# Николай решил вспомнить старые времена. 
# В свое время было модно писать сообщения с чередующимися заглавной и малой буквами. 
# Он захотел изобрести функцию, которая будет делать с любой предоставленной строкой аналогичное. 
# Ваша задача: повторить труд студента camel(st) с учетом того, что пробелы и знаки препинания не должны портить чередование регистра символов (они в этом процессе не учитываются, но возвращаются в итоговой строке).


def camel(st):
    new_st = ''
    letter_counter = 0
    for index, val in enumerate(st):
        if val.isalpha():
            if letter_counter % 2 == 0:
                new_st += val.upper()
            else:
                new_st += val.lower()
            letter_counter += 1
        else:
            new_st += val
    return new_st


print(camel('Утром!! было! солнечно!!!!'))  # УтРоМ!! бЫлО! сОлНеЧнО!!!!
print(camel('КРАСОТА)))'))  # КрАсОтА)))
print(camel('дождливЫЙ, вечеР??'))  # ДоЖдЛиВыЙ, вЕчЕр??