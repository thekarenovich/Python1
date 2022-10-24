# Александр решил как-то отобразить в тексте BACKSPACE (т.е. удаление последнего символа). 
# Он подумал, что символ «@» отлично для этого подходит. 
# Всем своим знакомым он дал строки такого вида (например, «гр@оо@лк@оц@ва»), чтобы посмотреть, кому удастся написать функцию cleaned_str(st), возвращающую строку в ее чистом виде.

def cleaned_str(st):
    clean_lst = []
    for symbol in st:
        if symbol == '@' and clean_lst:
            clean_lst.pop()
        elif symbol != '@':
            clean_lst.append(symbol)
    return ''.join(clean_lst)
  

# Альтернатива:
# s = 'сварка@@@@@лоб@ну@'
# while '@' in s:
#     sym = s.find('@')
#     s = s.replace(s[sym-1:sym+1], '')

print(cleaned_str('гр@оо@лк@оц@ва'))  # голова
print(cleaned_str('сварка@@@@@лоб@ну@'))  # слон

