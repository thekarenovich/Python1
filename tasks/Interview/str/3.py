# На основании предоставленного отрывка текста определить 3 наиболее часто встречаемых символа в ней. 
# Пробелы нужно игнорировать (не учитывать при подсчете). 
# Для выведения результатов вычислений требуется написать функцию top3(st). 
# Итог работы функции представить в виде строки: «символ – количество раз, символ – количество раз…».

from collections import Counter


def top3(st):
    counter_top3 = Counter(st.replace(' ', '')).most_common(3)
    return ', '.join([f'{letter} - {cnt}' for letter, cnt in counter_top3])
  

# Альтернатива:
# s = 'Голова думала'

# d = {}

# for k in range(3):
#     if(s):
#         maxi = 0
#         maxi_el = None
#         for item in s.replace(' ', ''):
#             if s.count(item) > maxi:
#                 maxi = s.count(item)
#                 maxi_el = item
#         d[maxi_el] = maxi
#         s = s.replace(maxi_el, '')
#     else:
#         break


print(top3('Улыбкой ясною природа Сквозь сон встречает утро года Синея блещут небеса. Еще прозрачные, леса'))  # е - 9, о - 8, р - 6
print(top3('АаА'))  # А - 2, а - 1
print(top3('Голова думала'))  # А - 3, о - 2, л - 2
