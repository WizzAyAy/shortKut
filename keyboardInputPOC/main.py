import tkinter as tk

import pygetwindow as gw
from pyautogui import keyDown, keyUp

# Create the master object
master = tk.Tk()

master.geometry("1000x300")
master.wm_state('iconic')


def button_callback(app_title, keys_input):
    print("ACTION SUR LE BOUTON : " + app_title)
    window = gw.getWindowsWithTitle(app_title)[0]
    master.iconify()

    window.maximize()
    window.activate()
    for key in keys_input:
        keyDown(key)
    for key in keys_input:
        keyUp(key)


titles = gw.getAllTitles()

i = 0
keys = [
    ['ctrl', 'c'],
    ['ctrl', 'v'],
    ['ctrl', 'a']
]

for title in titles:
    if title != '':
        tk.Button(master, text=title, command=lambda t=title, k=keys[2]: button_callback(t, k)).pack()
        # tk.Button(master, text=title, command=).pack()

tk.mainloop()
