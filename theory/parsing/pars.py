import requests # позволяет использовать HTTP в своих программах Python
from bs4 import BeautifulSoup # создает дерево синтаксического разбора из проанализированных HTML и XML-документов
# Эта библиотека сделает текст веб-страницы, извлеченный с помощью Requests, более удобочитаемым.

url = 'https://assets.digitalocean.com/articles/eng_python/beautiful-soup/mockturtle.html'
eriks_page = requests.get(url)

# print(eriks_page.status_code) 
# Возвращаемый код 200 сообщает, что страница загружена успешно
# Коды, начинающиеся с номера 2, обычно указывают на успешное выполнение операции
# A коды, начинающиеся с 4 или 5, сообщают об ошибке

# print(eriks_page.text)
# Полный текст страницы был отображен со всеми тегами HTML
# Однако его трудно прочитать, поскольку между ними не так много пробелов

soup = BeautifulSoup(eriks_page.text, 'html.parser')

# print(soup.prettify())
# Затем нужно запустить обработку документа page.text, чтобы получить объект BeautifulSoup
# То есть дерево синтаксического разбора этой страницы, полученной с помощью встроенного html.parser через HTML

# print(soup.find_all('p'))
# print(soup.find_all('p', class_='chorus'))
# print(soup.find_all(class_='chorus'))
# print(soup.find_all('p', id='third')) 
# Извлечь теги со страницы можно с помощью метода find_all
# Он вернет все экземпляры данного тега в документе
# В выводе вы увидите, что данные содержатся в квадратных скобках []. Этот тип данных Python называется списками.
# Применив этот метод, вы получите полный текст с соответствующими тегами <p> и любыми тегами, содержащимися в этом запрошенном теге

# find() работает также, но возвращает первый совпавший тег
# find.parent(), find.parents() возвращает родителя(ей) тега
# find.next() возвращает следующий элемент в коде
# find_next_sibling(), find_previous_sibling() возвращает следующий(предыдущий) блок кода элемента


# Вы можете вызвать определенный элемент списка (например, третий элемент <p>)
# И использовать метод get_text () для извлечения всего текста из этого тега

print(soup.find_all('p')[2].text)
# print(soup.select('p')[2].get_text())
'''
for i in range(len(soup.find_all('p'))):
	print(soup.find_all('p')[i].get_text())
'''
