import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def update_c_label(ev):
    code = combobox.get()
    name = cur[code]
    c_label.config(text=name)

def exchange():
    code = combobox.get()
    if code:
        try:
            response = requests.get("https://open.er-api.com/v6/latest/USD")
            response.raise_for_status()
            data = response.json()
            if code in data["rates"]:
                exchange_rate = data["rates"][code]
                c_name = cur[code]
                mb.showinfo("Курс обмена", f'Курс: {exchange_rate:.2f} {c_name} за 1 долар')
            else:
                mb.showerror("Ошибка!", f"Валюта {code} не найдена!")
        except Exception as e:
            mb.showerror("Ошибка!", f"Произошла ошибка: {e}")
    else:
        mb.showwarning("Внимание!", "Введите код валюты")


cur = {'RUB': 'Российский рубль',
       'EUR':'Евро',
       'GBP': 'Британский фунд стерлингов',
       'JPY': 'Японская йена',
       'CNY': 'Китайский юань',
       'KZT': 'Казахстанский тенге',
       'UZS': 'Узбетский сум',
       'CHF': 'Швецарский франк',
       'AED': 'Дирхам АОЭ',
       'CAD': 'Канадский долар'}

window = Tk()
window.title("Курс обмена валют")
window.geometry("360x180")

Label(text="Выберете код валюты").pack(padx=10, pady=10)


combobox = ttk.Combobox(values=list(cur.keys()))
combobox.pack(pady=10, padx=10)
combobox.bind("<<ComboboxSelected>>", update_c_label)

c_label = ttk.Label()
c_label.pack(pady=10, padx=10)

Button(text="Получить курс обмена к долору", command=exchange).pack(padx=10, pady=10)

window.mainloop()