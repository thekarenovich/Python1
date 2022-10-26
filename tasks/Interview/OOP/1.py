class Soda:
    def __init__(self, ingredient):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None

    def show_my_drink(self):
        if self.ingredient:
            print(f'Газировка и {self.ingredient}')
        else:
            print('Обычная газировка')

# drink1 = Soda()
# drink2 = Soda('малина')
# drink3 = Soda(5)
# drink1.show_my_drink()
# drink2.show_my_drink()
# drink3.show_my_drink()
# Результат выполнения
# Обычная газировка
# Газировка и малина
# Обычная газировка
