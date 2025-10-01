import requests
import json
from tkinter import *
from tkinter import messagebox as mb


def exchange()


window = Tk()
window.title("Курс обмена валют")
window.geometry("360x180")

Label(text="Введите код валюты").pack(padx=10, pady=10)

entry = Entry()
entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена к долору", command=exchange).pack(padx=10, pady=10)

window.mainloop()