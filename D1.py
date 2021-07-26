from datetime import datetime, date, time

def log(key,info):
    f = open("text.txt","a")
    if key == "CRE":
        a = ("{} --- {} --- {} {} {}\n".format("CRE",datetime.now(),"Экземпляр класс", info,"создан"))
        f.write(a)
    if key == "INF":
        b = ("{} --- {} --- {} {}\n".format("INF",datetime.now(),"Изменено",info))
        f.write(b)
    if key == "PRI":
        c = ("{} --- {} --- {} {}\n".format("PRI",datetime.now(),"Напечатано",info))
        f.write(c)
    if key == "ERR":
        d = ("{} --- {} --- {} {}\n".format("ERR",datetime.now(),"Ошибка",info))
        f.write(d)
    if key == "DEL":
        e = ("{} --- {} --- {} {}\n".format("DEL",datetime.now(),"Удален",info))
        f.write(e)
    f.close()
