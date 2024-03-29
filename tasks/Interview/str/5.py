# Дмитрий считает, что когда текст пишут в скобках (как вот тут, например), его читать не нужно. 
# Вот и надумал он существенно укоротить время чтения, написав функцию, которая будет удалять все, что расположено внутри скобок. 
# Помогите ленивому Диме разработать функцию shortener(st), которая будет удалять все, что внутри скобок и сами эти скобки, возвращая очищенный текст (скобки могут быть вложенными).

def shortener(st):
    while '(' in st or ')' in st:
        left = st.rfind('(')
        right = st.find(')', left)
        st = st.replace(st[left:right + 1], '')
    return st


print(shortener('Падал(лишнее (лишнее) лишнее) прошлогодний снег (лишнее)'))  # Падал прошлогодний снег 
print(shortener('(лишнее(лишнее))Падал прошлогодний (лишнее(лишнее(лишнее)))снег'))  # Падал прошлогодний снег 
