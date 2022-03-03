# в строке должна быть буква из списка letters_of_grups, 2-4 цифр
# не обращаем внимание на остальные буквы группы, слово "Вариант" и дефис

import string

letter = list(string.ascii_letters)

digits = list(string.digits)

letter_of_groups = ['К','Н','М','В','к','н','м','в']

numbers = [i for i in range(1,30+1)]
for i in range(len(numbers)):
    numbers[i] = str(numbers[i])

bad_subj = ['main.py', 'k17 14', 'K13 18', 'к02 1', 'ИВБО-11 Вариант№14', 'к02 21', '1.3.py', 'В 11 4', '\ufeff\u200b\u200bк20 21', 'B7 21',
            'Фамилия Имя Задача 1.1', 'В03 12', 'к08 24', 'к07 23', '1.2.py, 1.3.py, 1.4.py', '1.1.py', 'K14 23', 'в7 ', 'к6 ',
            '\u200b\u200bк20 21', 'к2 в3', 'В104', 'В1013', 'B3 29', 'v10 15', 'k13 30', 'В 7 10', 'Фамилия И.О. к7 31', '1.2.py', 'К10',
            'ПитонН4 н11', 'K13 28', 'К4', 'K17 10', 'и4 11', 'Н1', 'н01 28', 'б3 5', 'Re: в6 28', 'к-11 3', '2_1.py, 2_2.py']

new_bad_subj = []
for i in range(len(bad_subj)):
    t = True
    for j in range(len(letter)):
        if letter[j] in bad_subj[i]:
            t = False
    if t:
        new_bad_subj.append(bad_subj[i])
# new_bad_subj:
# ['к02 1', 'ИВБО-11 Вариант№14', 'к02 21', 'В 11 4', '\ufeff\u200b\u200bк20 21',
# 'Фамилия Имя Задача 1.1', 'В03 12', 'к08 24', 'к07 23', 'в7 ', 'к6 ', '\u200b\u200bк20 21', 'к2 в3',
# 'В104', 'В1013', 'В 7 10', 'Фамилия И.О. к7 31', 'К10', 'ПитонН4 н11', 'К4', 'и4 11', 'Н1', 'н01 28', 'б3 5', 'к-11 3']


newnew_bad_subj = []        
for i in range(len(new_bad_subj)):
    t = False
    for j in range(len(letter_of_groups)):
        if letter_of_groups[j] in new_bad_subj[i]:
            t = True
    if t == True:
        newnew_bad_subj.append(new_bad_subj[i])
# newnew_bad_subj:
# ['к02 1', 'ИВБО-11 Вариант№14', 'к02 21', 'В 11 4', '\ufeff\u200b\u200bк20 21',           'Фамилия Имя Задача 1.1',
#'В03 12', 'к08 24', 'к07 23',                                                              'в7 ', 'к6 ',
# '\u200b\u200bк20 21', 'к2 в3', 'В104', 'В1013', 'В 7 10', 'Фамилия И.О. к7 31',           'К10',
#'ПитонН4 н11',                                                                             'К4', 'Н1',
#'н01 28', 
#'к-11 3']


newnewnew_bad_subj = []
for i in range(len(newnew_bad_subj)):
    k = 0
    for j in numbers:
        if j in newnew_bad_subj[i]:
            k += 1
            if k >= 2:
                newnewnew_bad_subj.append(newnew_bad_subj[i])
                break
# newnewnew_bad_subj:
# ['к02 1', 'ИВБО-11 Вариант№14', 'к02 21', 'В 11 4', '\ufeff\u200b\u200bк20 21', 'В03 12', 'к08 24', 'к07 23', '\u200b\u200bк20 21',
# 'к2 в3', 'В104', 'В1013', 'В 7 10', 'Фамилия И.О. к7 31',                                                                             'К10',
# 'ПитонН4 н11', 'н01 28', 'к-11 3']


'''if len(str_digit1) + len(str_digit2) > kdig (количество цифр в строке) -> k-=1'''
end = []
for i in range(len(newnewnew_bad_subj)):
    k = 0
    for_checking = 0
    for j in numbers:
        if j in newnewnew_bad_subj[i]:
            k += 1
            for_checking += len(j)
    if k >= 2:
        kdig=0
        for a in range(len(newnewnew_bad_subj[i])):
            if(newnewnew_bad_subj[i][a] in digits):
                kdig+=1
        if for_checking > kdig:
            k-=1
        if k>=2:
            end.append(newnewnew_bad_subj[i])
# end:
# ['к02 1', 'ИВБО-11 Вариант№14', 'к02 21', 'В 11 4', '\ufeff\u200b\u200bк20 21', 'В03 12', 'к08 24', 'к07 23',
# '\u200b\u200bк20 21', 'к2 в3', 'В104', 'В1013', 'В 7 10', 'Фамилия И.О. к7 31', 'ПитонН4 н11', 'н01 28', 'к-11 3']

v = []
k = []
m = []
n = []

for i in range(len(end)):
    if('к' in end[i] or 'К' in end[i]):
        k.append(end[i])
    elif('в' in end[i] or 'В' in end[i]):
        v.append(end[i])
    elif('м' in end[i] or 'М' in end[i]):
        m.append(end[i])
    elif('н' in end[i] or 'Н' in end[i]):
        n.append(end[i])

# k:
# ['к02 1', 'к02 21', '\ufeff\u200b\u200bк20 21', 'к08 24', 'к07 23', '\u200b\u200bк20 21', 'к2 в3', 'Фамилия И.О. к7 31', 'к-11 3']

# v:
# ['ИВБО-11 Вариант№14', 'В 11 4', 'В03 12', 'В104', 'В1013', 'В 7 10']

# n:
# ['ПитонН4 н11', 'н01 28']

# m:
# []

if(k != []):
    sk = []
    for i in k:
        s = ''
        for j in i:
            if(j in digits or j == " "):
                s += j
        sk.append(s)

if(v != []):
    sv = []
    for i in v:
        s = ''
        for j in i:
            if(j in digits or j == " "):
                s += j
        sv.append(s)

if(n != []):
    sn = []
    for i in n:
        s = ''
        for j in i:
            if(j in digits or j == " "):
                s += j
        sn.append(s)

if(m != []):
    sm = []
    for i in m:
        s = ''
        for j in i:
            if(j in digits or j == " "):
                s += j
        sm.append(s)


for i in range(len(sk)):
    if(sk[i][0] == " " and sk[i][1] == " "):
        string = ''
        for j in range(0+2, len(sk[i])):
            string += sk[i][j]
        sk[i]=string
    elif(sk[i][0] == " "):
        string = ''
        for j in range(0+1, len(sk[i])):
            string += sk[i][j]
        sk[i]=string

for i in range(len(sv)):
    if(sv[i][0] == " " and sv[i][1] == " "):
        string = ''
        for j in range(0+2, len(sv[i])):
            string += sv[i][j]
        sv[i]=string
    elif(sv[i][0] == " "):
        string = ''
        for j in range(0+1, len(sv[i])):
            string += sv[i][j]
        sv[i]=string

for i in range(len(sn)):
    if(sn[i][0] == " " and sn[i][1] == " "):
        string = ''
        for j in range(0+2, len(sn[i])):
            string += sn[i][j]
        sn[i]=string
    elif(sn[i][0] == " "):
        string = ''
        for j in range(0+1, len(sn[i])):
            string += sn[i][j]
        sn[i]=string

# sk: ['02 1', '02 21', '20 21', '08 24', '07 23', '20 21', '2 3', '7 31', '11 3']
# sv: ['11 14', '11 4', '03 12', '104', '1013', '7 10']
# sn: ['4 11', '01 28']


for i in range(len(sk)):
    num1=''
    num2=''
    if((len(sk[i]) == 4 and " " in sk[i])  or (len(sk[i]) == 3 and " " not in sk[i])): # три цифры в строке
        if len(sk[i]) == 4 and " " in sk[i]:
            if sk[i][1] != ' ':
                num1 = sk[i][0] + sk[i][1]
                num2 = sk[i][3]
            else:
                num1 = '0' + sk[i][0]
                num2 = sk[i][2] + sk[i][3]
        elif len(sk[i]) == 3 and " " not in sk[i]:
            num1 = sk[i][0] + sk[i][1]
            num2 = sk[i][2]
    if(num1!='' and num2!=''):
        print(f'ИКБО-{num1}-20 Вариант№{num2}')

for i in range(len(sn)):
    num1=''
    num2=''
    if((len(sn[i]) == 4 and " " in sn[i])  or (len(sn[i]) == 3 and " " not in sn[i])): # три цифры в строке
        if len(sn[i]) == 4 and " " in sn[i]:
            if sn[i][1] != ' ':
                num1 = sn[i][0] + sn[i][1]
                num2 = sn[i][3]
            else:
                num1 = '0' + sn[i][0]
                num2 = sn[i][2] + sn[i][3]
        elif len(sn[i]) == 3 and " " not in sn[i]:
            num1 = sn[i][0] + sn[i][1]
            num2 = sn[i][2]
    if(num1!='' and num2!=''):
        print(f'ИНБО-{num1}-20 Вариант№{num2}')

for i in range(len(sv)):
    num1=''
    num2=''
    if((len(sv[i]) == 4 and " " in sv[i])  or (len(sv[i]) == 3 and " " not in sv[i])): # три цифры в строке
        if len(sv[i]) == 4 and " " in sv[i]:
            if sv[i][1] != ' ':
                num1 = sv[i][0] + sv[i][1]
                num2 = sv[i][3]
            else:
                num1 = '0' + sv[i][0]
                num2 = sv[i][2] + sv[i][3]
        elif len(sv[i]) == 3 and " " not in sv[i]:
            num1 = sv[i][0] + sv[i][1]
            num2 = sv[i][2]
    if(num1!='' and num2!=''):
        print(f'ИВБО-{num1}-20 Вариант№{num2}')

if(k != []):
    for i in range(len(sk)):
        if( len(sk[i]) != 4 ):
            sk[i]=sk[i].replace(" ", "")
if(n != []):
    for i in range(len(sn)):
        if( len(sn[i]) != 4 ):
            sn[i]=sn[i].replace(" ", "")
if(v != []):
    for i in range(len(sv)):
        if( len(sv[i]) != 4 ):
            sv[i]=sv[i].replace(" ", "")
if(m != []):
    for i in range(len(sm)):
        if( len(sm[i]) != 4 ):
            sm[i]=sm[i].replace(" ", "")

for i in range(len(sk)):
    
    num1 = ''
    num2 = ''
    
    if(len(sk[i]) == 4 and ' ' not in sk[i]):
        num1 = sk[i][0] + sk[i][1]
        num2 = sk[i][2] + sk[i][3]
    elif(len(sk[i]) == 2):
        num1 = '0' + sk[i][0]
        num2 = sk[i][1]

    if(num1 != '' and num2 != ''):
        print(f'ИКБО-{num1}-20 Вариант№{num2}')

for i in range(len(sv)):
    
    num1 = ''
    num2 = ''
    
    if(len(sv[i]) == 4 and ' ' not in sv[i]):
        num1 = sv[i][0] + sv[i][1]
        num2 = sv[i][2] + sv[i][3]
    elif(len(sv[i]) == 2):
        num1 = sv[i][0]
        num2 = sv[i][1]

    if(num1 != '' and num2 != ''):
        print(f'ИВБО-{num1}-20 Вариант№{num2}')

for i in range(len(sn)):
    
    num1 = ''
    num2 = ''
    
    if(len(sn[i]) == 4 and ' ' not in sn[i]):
        num1 = sn[i][0] + sn[i][1]
        num2 = sn[i][2] + sn[i][3]
    elif(len(sk[i]) == 2):
        num1 = sn[i][0]
        num2 = sn[i][1]

    if(num1 != '' and num2 != ''):
        print(f'ИНБО-{num1}-20 Вариант№{num2}')

'''
ИКБО-02-20 Вариант№1
ИКБО-07-20 Вариант№31
ИКБО-11-20 Вариант№3
ИНБО-04-20 Вариант№11
ИВБО-11-20 Вариант№4
ИВБО-10-20 Вариант№4
ИВБО-07-20 Вариант№10
ИКБО-02-20 Вариант№21
ИКБО-20-20 Вариант№21
ИКБО-08-20 Вариант№24
ИКБО-07-20 Вариант№23
ИКБО-20-20 Вариант№21
ИКБО-02-20 Вариант№3
ИВБО-11-20 Вариант№14
ИВБО-03-20 Вариант№12
ИВБО-10-20 Вариант№13
ИНБО-01-20 Вариант№28
'''
