# При помощи библиотеки Pillow в директории circles (создайте ее во время выполнения функции) нарисуйте и сохраните 100 кругов радиусом 300 пикселей случайных цветов в формате jpg на белом фоне (каждый круг - отдельный файл). 
# Для этого напишите функцию circles_generator(num_of_circles=100).

from random import randint
import os
from PIL import Image, ImageDraw
 
 
def circles_generator(num_of_circles=100):

    if not os.path.exists('circles'):
        os.mkdir('circles')

    for pic_name in range(1, num_of_circles + 1):
        img = Image.new('RGB', (600, 600), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        draw.ellipse((0, 0, 600, 600), fill=(randint(0, 255), randint(0, 255), randint(0, 255)))
        img.save(f'circles/{pic_name}.jpg', quality=85)
 
 
circles_generator()

# В результате выполнения скрипта в папке circles появится 100 картинок кругов одинакового размера.
# При повторном вызове программы ошибки не будет, так как мы создаем папку лишь в том случае, если ее нет.
