import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def update_c_label(ev):
    code = t_combobox.get()
    name = cur[code]
    c_label.config(text=name)

def exchange():
    t_code = t_combobox.get()
    b_code = b_combobox.get()
    if t_code and b_code:
        try:
            response = requests.get(f"https://open.er-api.com/v6/latest/{b_code}")
            response.raise_for_status()
            data = response.json()
            if t_code in data["rates"]:
                exchange_rate = data["rates"][t_code]
                t_name = cur[t_code]
                b_name = cur[b_code]
                mb.showinfo("Курс обмена", f'Курс: {exchange_rate:.2f} {t_name} за 1 {b_name}')
            else:
                mb.showerror("Ошибка!", f"Валюта {t_code} не найдена!")
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
       'CAD': 'Канадский долар',
       'USD': 'Американский долар'}

window = Tk()
window.title("Курс обмена валют")
window.geometry("360x300")

Label(text="Базовая валюта").pack(padx=10, pady=10)

b_combobox = ttk.Combobox(values=list(cur.keys()))
b_combobox.pack(pady=10, padx=10)

Label(text="Целевая валюта").pack(padx=10, pady=10)

t_combobox = ttk.Combobox(values=list(cur.keys()))
t_combobox.pack(pady=10, padx=10)
t_combobox.bind("<<ComboboxSelected>>", update_c_label)

c_label = ttk.Label()
c_label.pack(pady=10, padx=10)

Button(text="Получить курс обмена ", command=exchange).pack(padx=10, pady=10)

window.mainloop()