# в терминале linux вводим pip3 install pygame для того, чтобы могли работать с pygame
import tkinter as tk
from tkinter import filedialog
from pygame import mixer
     
    
    
    

def load():
    global music_file
    music_file = filedialog.askopenfilename()
    Chosen = tk.Label(window, text="Music is chosen", fg='black', font=('Calibri', 10, 'bold'))
    Chosen.place(x=75, y=10)

    # выбираем муз. файл для прослушивания


def play():
    if music_file:
        #global status
        #status = value
        mixer.init()
        mixer.music.load(music_file)
        mixer.music.play()
        Play.destroy()
        Pause = tk.Button(window, text='Pause', width=12, font=('Times', 23, 'bold'), command=pause)
        Pause.place(x=45, y=35)
    # запуск мелодии

def pause():
    global playing_state
    if playing_state == False:
        Pause = tk.Button(window, text='Play', width=12, font=('Times', 23, 'bold'), command=pause)
        Pause.place(x=45, y=35)
        mixer.init()
        mixer.music.pause()
        playing_state = True
    else:
        Pause = tk.Button(window, text='Pause', width=12, font=('Times', 23, 'bold'), command=pause)
        Pause.place(x=45, y=35)
        mixer.init()
        mixer.music.unpause()
        playing_state = False
    # пауза и запуск мелодии


def stop():
    mixer.music.stop()
    window.destroy()
    # убирание мелодии
    # закрытие окна


window = tk.Tk()
window.title('   Music Player')
window.geometry('235x100')
window.resizable(False,False)

music_file = False
playing_state = False
status = False

Load = tk.Button(window, text = 'Choose',  width = 10, font = ('Times', 10, 'bold'), command = load)
Load.place(x=10, y=10)
Play = tk.Button(window, text = 'Play',  width = 12,font = ('Times', 23, 'bold'), command =play )
Play.place(x=45, y=35)
'''Pause = tk.Button(window, text = 'Pause',  width = 10, font = ('Times', 17, 'bold'), command = )
Pause.place(x=130,y=40)'''
Stop = tk.Button(window, text = 'Quiet',  width = 7, font = ('Times', 8, 'bold'), command = stop)
Stop.place(x=107,y=75)


#app = MusicPlayer(root)
window.mainloop()

