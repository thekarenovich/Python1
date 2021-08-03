import sqlite3
 
ccc = sqlite3.connect("erik_db.db") # связь с бд функцией connect
aaa = ccc.cursor() # взаимодейсвтие с бд
# aaa или другое любое название будет использоваться с execute
# execute - функция используется для действий с таблицей 
 
aaa.execute("""CREATE TABLE albums
                  (title text, artist text, release_date text,
                   publisher text, media_type text)
               """)

# у нас теперь таблца albums c полями типа text
# строку можно вставить в виде переменной со значением данной строки также
# так будет, куда удобней и симпатичней
# а сама строка это чистый SQLite
# однако нам доступны лишь 5 типов данных:
# null, real(вещ. числа), text, integer, blob(что-то с байтами)


aaa.execute('''INSERT INTO albums VALUES
          ('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
          ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
          ('The End is Where We Begin', 'Thousand Foot Krutch', '4/17/2012', 'TFKmusic', 'CD'),
          ('The Good Life', 'Trip Lee', '4/10/2012', 'Reach Records', 'CD')''')


ccc.commit()

something = """
UPDATE albums 
SET artist = 'John Doe' 
WHERE artist = 'Andy Hunter'
"""

aaa.execute(something)
ccc.commit()

something = "DELETE FROM albums WHERE artist = 'John Doe'"
 
aaa.execute(something)
ccc.commit()

something = "SELECT * FROM albums"
aaa.execute(something)
print(aaa.fetchall())
