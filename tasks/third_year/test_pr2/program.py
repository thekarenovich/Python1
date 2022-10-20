class Topics:
    def choose_topic(self, a):
        if a == 1:
            return "Стриминговый сервис"
        elif a == 2:
            return "Университет"
        elif a == 3:
            return "Кубик Рубика"


class Uni:
    def uni_method(self, g1, g2, g3, g4):
        print("Я забыл, ты где учишься. В мирэа или ранхигс ?(мирэа/ранхигс)")
        g1 = str(input())
        if g1.lower().replace(" ", "") == "ранхигс":
            return "ПОКА))))"
        elif g1.lower().replace(" ", "") == "мирэа":
            print("Значит программист?(да/нет)")
            g2 = str(input())
            if g2.lower().replace(" ", "") == "нет":
                return "Fuck, кто же мне тогда принтер починит ..."
            elif g2.lower().replace(" ", "") == "да":
                print("Python - дерьмо?(да/нет)")
                g3 = str(input())
                if g3.lower().replace(" ", "") == "нет":
                    return "Неправильно ))))))"
                elif g3.lower().replace(" ", "") == "да":
                    print("Красавец! А почему я написан на нем?))(да/да)")
                    g4 = str(input())
                    if g4.lower().replace(" ", "") == "да":
                        return "ХАХАХАХАХАХ"


class Stream:
    def stream_method(self, v1, v2, v3, v4, v5):
        print("В стрим. сервисах смотришь больше кино или сериалы?(кино/сериалы)")
        v1 = str(input())
        if v1.lower().replace(" ", "") == "кино":
            print("Ты успел посмотреть 'Черного Адама'?(да/нет)")
            v2 = str(input())
            if v2.lower().replace(" ", "") == "нет":
                return "Отлично! Вместе посмотрим тогда)"
            elif v2.lower().replace(" ", "") == "да":
                print("О, как тебе?(классный/пойдет/ужас)")
                v3 = str(input())
                if v3.lower().replace(" ", "") == "классный":
                    return "Так и знал) Точно гляну"
                elif v3.lower().replace(" ", "") == "пойдет":
                    return "Ох, надеюсь, получше все-таки"
                elif v3.lower().replace(" ", "") == "ужас":
                    return "Мда уж, DC скатились, досадно"

        elif v1.lower().replace(" ", "") == "сериалы":
            print("Тебе нравится больше 'Элита' или 'Ривердейл'?(элита/ривердейл)")
            v4 = str(input())
            if v4.lower().replace(" ", "") == "ривердейл":
                return "Друг, нам не о чем говорить, аххахахаа!"
            elif v4.lower().replace(" ", "") == "элита":
                print("Хороший вкус) Все сезоны смотрел?(да/нет)")
                v5 = str(input())
                if v5.lower().replace(" ", "") == "да":
                    return "Ждем новые тогда) Классно поговорили, спасибо)"
                elif v5.lower().replace(" ", "") == "нет":
                    return "Давай, догоняй меня)) Классно поговорили, спасибо)"


class Rubik:
    def rubik_method(self, r1, r2, r3):
        print("Собираешь кубик Рубика?(да/нет)")
        r1 = str(input())
        if r1.lower().replace(" ", "") == "нет":
            return "Досадно:( Тогда лучше о другом поговорить, хах"
        elif r1.lower().replace(" ", "") == "да":
            print("На скорость собираешь?(да/нет)")
            r2 = str(input())
            if r2.lower().replace(" ", "") == "да":
                return "Чувак, ты крут))"
            elif r2.lower().replace(" ", "") == "нет":
                print("А не планируешь более профессионально этим заняться?(да/нет)")
                r3 = str(input())
                if r3.lower().replace(" ", "") == "да":
                    return "Успехов там) Спортивные ручки будут Классно поговорили, спасибо)"
                elif r3.lower().replace(" ", "") == "нет":
                    return "Тогда у тебя просто хорошее хобби) Молодец! Классно поговорили, спасибо)"


def main():
    topic = Topics()
    rubik = Rubik()
    uni = Uni()
    stream = Stream()
    print("""
    Привет! Я TheKarenovich 
    Рад тебя видеть, давай пообщаемся:) 
    Мои любимые темы: 1.Стриминговый сервис, 2.Университет, 3.Кубик Рубика
    Напиши цифру полюбившейся темы:)
    """)

    a = int(input())

    if topic.choose_topic(a) == "Стриминговый сервис":
        print(stream.stream_method(v1=str(), v2=str(), v3=str, v4=str, v5=str), "\n")
    elif topic.choose_topic(a) == "Университет":
        print(uni.uni_method(g1=str(), g2=str(), g3=str(), g4=str()), "\n")
    elif topic.choose_topic(a) == "Кубик Рубика":
        print(rubik.rubik_method(r1=str, r2=str, r3=str), "\n")


if __name__ == '__main__':
    main()
