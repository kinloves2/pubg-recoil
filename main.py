# encoding: utf-8
import win32api
import mouse
import random
import os

import tkinter as tk
from tkinter import *
from time import sleep
from random import randint
from tkinter import messagebox
from tkinter import filedialog


# Macro ---------------------------------------------------------------------------------------------------------------

def macro():
    #Text
    print('----------------------------------------------------------------')
    print('|------Это простой макрос для помощи в Pubg------|')
    print('|------Нажмите клавишу X, чтобы включить и выключить макрос.------')
    # Recoil

    m416 = [37.1, 24.7, 27.2, 29.7, 32.1, 39.6, 39.6, 39.6, 39.6, 39.6, 39.6, 42, 42, 42, 42, 42, 42, 44.5, 44.5, 44.5,
            44.5, 44.5, 44.5, 45.7, 45.7, 45.7, 45.7, 45.7, 45.7, 45.7, 47, 47, 47, 47, 49.4, 49.4, 49.4, 49.4, 49.4, 49.4, 49.4]

    # vars
    count = 0
    EinAus = False
    jaornein = randint(0, 1)

    # Loop
    count = 0
    while True:
        if win32api.GetAsyncKeyState(ord('X')):
            EinAus = not EinAus
            sleep(0.2)
            print('On')
        sleep(0.2)
        while EinAus is True:
            count = 0
            while mouse.is_pressed(button='left'):
                if count < 40:
                    jaornein = randint(0, 1)
                    if jaornein == 1:
                        randomized = randint(0, 5)
                    elif jaornein == 0:
                        randomized = random.uniform(0, -5)
                    print(randomized)
                    ammount = m416[count]
                    if jaornein == 1:
                        ammount = ammount + randomized
                    elif jaornein == 0:
                        ammount = ammount - randomized
                    ammountFinal = int(round(ammount))
                    win32api.mouse_event(0x0001, 0, ammountFinal)
                    sleep(0.10)
                count = count + 1
                if count > 40:
                    count = 0
                    ammount = 0
            if win32api.GetAsyncKeyState(ord('X')):
                print('Out')
                EinAus = not EinAus
                sleep(0.2)
                break
            sleep(0.1)





# Интерфейс -----------------------------------------------------------------------------------------------------------


mGui = Tk()
mGui.title("Rumonas Macro")
mGui.geometry('300x250')
mGui.resizable(False, False)


#Imagens
imagem = PhotoImage(file="fon.png")
image=imagem.subsample(1,1)
start = PhotoImage(file="run.png")
donat = PhotoImage(file="donations.png")
exit = PhotoImage(file="exit.png")



# funcao-don
def don():
    os.system("start \"\" http://www.donationalerts.ru/r/beha")
# end-func

# funcao-out
def out():
    out = sys.exit(0)
# end-func


# определение окна и рамки
class Application:

    def __init__(self, master=None):

        # Master
        self.widget1 = Label(master)
        self.widget1['image'] = imagem
        self.widget1.place(x=0,y=0,relwidth=1.0,relheight=1.0)

        # Заголовок
        self.msg = Label(self.widget1)
        self.msg['text'] = "RUMACRO 2018 v.01"
        self.msg['fg'] = '#4682B4'
        self.msg['bg'] = '#191970'
        self.msg["font"] = ("Courier New", 19, "bold")
        self.msg.place(x=20,y=0)

        # Обвновление
        self.msg = Label(self.widget1)
        self.msg['text'] = "Будут донаты->Будут обновления"
        self.msg['fg'] = '#4682B4'
        self.msg['bg'] = '#191970'
        self.msg["font"] = ("Courier New", 12, "bold")
        self.msg.place(x=-5,y=220)

        # Кнопка запуска
        self.startm = Button(self.widget1)
        self.startm["text"] = "Iniciar"
        self.startm["font"] = ("Verdana", "10")
        self.startm["width"] = 196
        self.startm["height"] = 51
        self.startm['bg'] = '#d49307'
        self.startm['image'] = start
        self.startm["command"] = macro
        self.startm.place(x=0, y = 138)

        # Кнопка доната
        self.donations = Button(self.widget1)
        self.donations['text'] = "DONAT"
        self.donations["width"] = 81
        self.donations["height"] = 34
        self.donations['bg'] = '#191970'
        self.donations['image'] = donat
        self.donations['command'] = don
        self.donations.place(x=211, y = 120)

        # Кнопка выхода
        self.exit = Button(self.widget1)
        self.exit['text'] = "Выйти"
        self.exit["width"] = 83
        self.exit["height"] = 29
        self.exit['bg'] = '#FF0000'
        self.exit['image'] = exit
        self.exit['command'] = out
        self.exit.place(x=211,y=178)





Application(mGui)
mGui.mainloop()
