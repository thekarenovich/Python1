# в терминале linux вводим pip3 install pygame для того, чтобы могли работать с pygame

from tkinter import *
from tkinter import filedialog
from pygame import mixer

root = Tk()

class MusicPlayer:

    def load(self):
        self.music_file = filedialog.askopenfilename()
        # выбираем муз. файл для прослушивания

    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
        # запуск мелодии

    def pause(self):
        if self.playing_state == False:
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state = False
        # пауза и запуск мелодии

    def stop(self):
        mixer.music.stop()
        root.destroy()
        # убирание мелодии
        # закрытие окна

    def __init__(self, window):
        window.title('  Music Player')
        window.geometry('235x100')
        window.resizable(False,False)

        Load = Button(window, text = 'Choose',  width = 10, font = ('Times', 10, 'bold'), command = self.load)
        Load.place(x=10, y=10)
        Play = Button(window, text = 'Play',  width = 10,font = ('Times', 17, 'bold'), command = self.play)
        Play.place(x=20, y=40)
        Pause = Button(window, text = 'Pause',  width = 10, font = ('Times', 17, 'bold'), command = self.pause)
        Pause.place(x=130,y=40)
        Stop = Button(window, text = 'Quiet',  width = 7, font = ('Times', 8, 'bold'), command = self.stop)
        Stop.place(x=107,y=75)

        self.music_file = False
        self.playing_state = False

app = MusicPlayer(root)
root.mainloop()
