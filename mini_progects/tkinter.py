from tkinter import *
from tkinter import ttk
from tkinter.ttk import Notebook
import urllib.request
import xml.dom.minidom

def get_valutes():
    valutes = {}

    response = urllib.request.urlopen('http://www.cbr.ru/scripts/XML_daily.asp?date_req=17/04/2021')
    dom = xml.dom.minidom.parse(response)

    ValCurs = dom.getElementsByTagName('ValCurs')[0]

    for Valute in ValCurs.getElementsByTagName('Valute'):
        Name = Valute.getElementsByTagName('Name')[0]
        Value = Valute.getElementsByTagName('Value')[0]

        valutes[Name.firstChild.nodeValue] = float(Value.firstChild.nodeValue.replace(',', '.'))

    return valutes

valutes = get_valutes()

def convert():
    valute_from = valutes[valute_from_combobox.get()]
    value_to = valutes[value_to_combobox.get()]

    ratio = valute_from / value_to

    value = float(value_entry.get())
    converted = round(value * ratio, 2)

    output_label.config(text=converted)


def level():
    m=(" ", " ", " ")

    if(x.get()==1):
        var1=ttk.Combobox(master=window_2, values=m)
        var1.current(1) #Для того, чтобы былр название в comboxe
        var1.grid(row=1, column=2, padx=5, pady=5)

        var = Label(
        master=window_2,
        text="  ",
        foreground="white", 
        background="white",  
        width=27, 
        height=2 )
        var.grid(row=2, column=2, padx=5, pady=5)

        var = Label(
        master=window_2,
        text="  ",
        foreground="white", 
        background="white",  
        width=27, 
        height=2 )
        var.grid(row=3, column=2, padx=5, pady=5)

        var = Label(
        master=window_2,
        text="  ",
        foreground="white", 
        background="white",  
        width=27, 
        height=2 )
        var.grid(row=4, column=2, padx=5, pady=5)


    elif(x.get()==2):
        var1=ttk.Combobox(master=window_2, values=m)
        var1.current(1) #Для того, чтобы былр название в comboxe
        var1.grid(row=2, column=2, padx=5, pady=5)

        var = Label(
        master=window_2,
        text="  ",
        foreground="white", 
        background="white",  
        width=27, 
        height=2 )
        var.grid(row=1, column=2, padx=5, pady=5)

        var = Label(
        master=window_2,
        text="  ",
        foreground="white", 
        background="white",  
        width=27, 
        height=2 )
        var.grid(row=3, column=2, padx=5, pady=5)

        var = Label(
        master=window_2,
        text="  ",
        foreground="white", 
        background="white",  
        width=27, 
        height=2 )
        var.grid(row=4, column=2, padx=5, pady=5)

        
    elif(x.get()==3):
        var1=ttk.Combobox(master=window_2, values=m)
        var1.current(1) #Для того, чтобы былр название в comboxe
        var1.grid(row=3, column=2, padx=5, pady=5)

        var = Label(
        master=window_2,
        text="  ",
        foreground="white", 
        background="white",  
        width=27, 
        height=2 )
        var.grid(row=2, column=2, padx=5, pady=5)

        var = Label(
        master=window_2,
        text="  ",
        foreground="white", 
        background="white",  
        width=27, 
        height=2 )
        var.grid(row=1, column=2, padx=5, pady=5)

        var = Label(
        master=window_2,
        text="  ",
        foreground="white", 
        background="white",  
        width=27, 
        height=2 )
        var.grid(row=4, column=2, padx=5, pady=5)

        
    elif(x.get()==4):
        var1=ttk.Combobox(master=window_2, values=m)
        var1.current(1) #Для того, чтобы былр название в comboxe
        var1.grid(row=4, column=2, padx=5, pady=5)

        var = Label(
        master=window_2,
        text="  ",
        foreground="white", 
        background="white",  
        width=27, 
        height=2 )
        var.grid(row=2, column=2, padx=5, pady=5)

        var = Label(
        master=window_2,
        text="  ",
        foreground="white", 
        background="white",  
        width=27, 
        height=2 )
        var.grid(row=3, column=2, padx=5, pady=5)

        var = Label(
        master=window_2,
        text="  ",
        foreground="white", 
        background="white",  
        width=27, 
        height=2 )
        var.grid(row=1, column=2, padx=5, pady=5)



window = Tk()
window.title("Application")
window.resizable(False, False)
window1 = Frame()

window2 = Notebook(window)
window_1 = Frame(window2, relief=FLAT, borderwidth=0)
window_2 = Frame(window2, relief=FLAT, borderwidth=0)
window2.add(window_1, text="Калькулятор валют")
window2.add(window_2, text="Динамика курса")
window2.pack(fill=BOTH, expand=1)

# Список 1 в 1 окне
m = list(valutes.keys())
window_1.rowconfigure(0, weight=1, minsize=50)
window_1.columnconfigure(0, weight=1, minsize=50)
valute_from = valute_from_combobox=ttk.Combobox(master=window_1, values=m)
valute_from = valute_from_combobox.current(1) #Для того, чтобы былр название в comboxe
valute_from = valute_from_combobox.grid(row=0, column=0, padx=5, pady=5)


# Список 2 в 1 окне
window_1.rowconfigure(1, weight=1, minsize=50)
window_1.columnconfigure(0, weight=1, minsize=50)
value_to_combobox=ttk.Combobox(master=window_1, values=m)
value_to_combobox.current(2) #Для того, чтобы былр название в comboxe
value_to_combobox.grid(row=1, column=0, padx=5, pady=5)


# Вывод результата в 1 окне
window_1.rowconfigure(1, weight=1, minsize=50)
window_1.columnconfigure(1, weight=1, minsize=50)
output_label = Label(
    master=window_1,
    text="Здесь результат",
    foreground="black", 
    # fg="white"
    background="white",  
    # bg="black"
    width=13, 
    height=1 
)
output_label.grid(row=1, column=1, padx=5, pady=5)


# Ввод в 1 окне
window_1.rowconfigure(0, weight=1, minsize=50)
window_1.columnconfigure(1, weight=1, minsize=50)
value_entry = Entry(master=window_1,
               #text="Textt",
               fg="black",
               bg="white",
               width=18
)
value_entry.grid(row=0, column=1, padx=5, pady=5)


# Кнопка в 1 окне
window_1.rowconfigure(1, weight=1, minsize=50)
window_1.columnconfigure(2, weight=1, minsize=50)
var = Button(master=window_1,
               text="Конвертировать",
               width=15, 
               height=1,
               fg="black",
               bg="white",
               activebackground="white",
               activeforeground="red",
               command=convert)
var.grid(row=1, column=2, padx=5, pady=5)


# Вывод "Валюта" в 2 окне 
#window_1.rowconfigure(2, weight=1, minsize=50)
#window_1.columnconfigure(1, weight=1, minsize=50)
var = Label(
    master=window_2,
    text="Валюта",
    foreground="black", 
    # fg="white"
    background="white",  
    # bg="black"
    width=13, 
    height=1 
)
var.grid(row=0, column=0, padx=5, pady=5)

# Вывод "Выбор периода" в 2 окне 
#window_1.rowconfigure(2, weight=1, minsize=50)
#window_1.columnconfigure(1, weight=1, minsize=50)
var = Label(
    master=window_2,
    text="Выбор периода",
    foreground="black", 
    # fg="white"
    background="white",  
    # bg="black"
    width=13, 
    height=1 
)
var.grid(row=0, column=2, padx=5, pady=5)

# Вывод "Период" в 2 окне 
#window_1.rowconfigure(2, weight=1, minsize=50)
#window_1.columnconfigure(1, weight=1, minsize=50)
var = Label(
    master=window_2,
    text="Период",
    foreground="black", 
    # fg="white"
    background="white",  
    # bg="black"
    width=13, 
    height=1 
)
var.grid(row=0, column=1, padx=5, pady=5)

# Список в 2 окне 
window_1.rowconfigure(0, weight=1, minsize=50)
window_1.columnconfigure(0, weight=1, minsize=50)
var1=ttk.Combobox(master=window_2, values=m)
var1.current(1) #Для того, чтобы былр название в comboxe
var1.grid(row=1, column=0, padx=5, pady=5)

# Пустой Вывод в 2 окне
#window_1.rowconfigure(2, weight=1, minsize=50)
#window_1.columnconfigure(1, weight=1, minsize=50)
var = Label(
    master=window_2,
    text=" ",
    foreground="white", 
    # fg="white"
    background="white",  
    # bg="black"
    width=13, 
    height=1 
)
var.grid(row=2, column=0, padx=5, pady=5)

# Пустой Вывод в 2 окне
#window_1.rowconfigure(2, weight=1, minsize=50)
#window_1.columnconfigure(1, weight=1, minsize=50)
var = Label(
    master=window_2,
    text=" ",
    foreground="white", 
    # fg="white"
    background="white",  
    # bg="black"
    width=13, 
    height=1 
)
var.grid(row=3, column=0, padx=5, pady=5)

# Кнопка в 2 окне
#window_1.rowconfigure(2, weight=1, minsize=50)
#window_1.columnconfigure(0, weight=1, minsize=50)
var = Button(master=window_2,
               text="Построить график",
               width=23, 
               height=1,
               fg="black",
               bg="white",
               activebackground="white",
               activeforeground="red")
var.grid(row=4, column=0, padx=5, pady=5)



# Вариации в 2 окне
#window_1.rowconfigure(2, weight=1, minsize=50)
#window_1.columnconfigure(0, weight=1, minsize=50)
var = Label(
master=window_2,
text="  ",
foreground="white", 
background="white",  
width=27, 
height=2 )
var.grid(row=1, column=2, padx=5, pady=5)

var = Label(
master=window_2,
text="  ",
foreground="white", 
background="white",  
width=27, 
height=2 )
var.grid(row=2, column=2, padx=5, pady=5)
    
var = Label(
master=window_2,
text="  ",
foreground="white", 
background="white",  
width=27, 
height=2 )
var.grid(row=3, column=2, padx=5, pady=5)

var = Label(
master=window_2,
text="  ",
foreground="white", 
background="white",  
width=27, 
height=2 )
var.grid(row=4, column=2, padx=5, pady=5)
    
x=IntVar()
Radiobutton(window_2, text="Неделя", variable=x, value=1, command=level).grid(row=1, column=1, padx=5, pady=5)
Radiobutton(window_2, text="Месяц", variable=x, value=2, command=level).grid(row=2, column=1, padx=5, pady=5)
Radiobutton(window_2, text="Квартал", variable=x, value=3, command=level).grid(row=3, column=1, padx=5, pady=5)
Radiobutton(window_2, text="Год", variable=x, value=4, command=level).grid(row=4, column=1, padx=5, pady=5)

window.mainloop()


