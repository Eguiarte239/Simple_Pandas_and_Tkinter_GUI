import tkinter as tk
from tkinter import END, ttk
from tkinter.colorchooser import *
from tkinter.ttk import *
import pandas as pd

df = pd.read_csv('usuarios.txt')

def on_field_change():
    if filtradoPrincipal.get() == "Edad":
        filtroSec.set('Filtrado por edad')
        filtroSec.place(x = 250, y = 15)
        btnSec.place(x = 272, y = 45, width=100, height=25)
    else:
        filtroSec.place_forget()
        btnSec.place_forget()
 
def filtrarPrincipal():
    on_field_change()
    if filtradoPrincipal.get() == "Edad":
        listbox.delete(0,END)
        shownData = list(df[['id','Nombre', 'Edad']].values)
        listbox.insert(END, "[id, Nombre, Edad]")
        for data in shownData:
            listbox.insert(END, '---------------------------------------------')
            listbox.insert(END, data)
    
    elif filtradoPrincipal.get() == "Ocupacion":
        listbox.delete(0,END)
        shownData = list(df[['id','Nombre', 'Ocupacion']].values)
        listbox.insert(END, "[id, Nombre, Ocupacion]")
        for data in shownData:
            listbox.insert(END, '--------------------------------------------------------')
            listbox.insert(END, data)


def filtrarSecundario(filtrado):
    if filtrado.get() == "15 - 44":
        listbox.delete(0,END)
        secondaryDf = df[df['Edad'].between(15, 44)]
        shownData = list(secondaryDf[['id', 'Nombre', 'Edad']].values)
        listbox.insert(END, "[id, Nombre]")
        for data in shownData:
            listbox.insert(END, '---------------------------------------------')
            listbox.insert(END, data)
    
    elif filtrado.get() == "45 - 84":
        listbox.delete(0,END)
        secondaryDf = df[df['Edad'].between(45, 84)]
        shownData = list(secondaryDf[['id', 'Nombre', 'Edad']].values)
        listbox.insert(END, "[id, Nombre]")
        for data in shownData:
            listbox.insert(END, '---------------------------------------------')
            listbox.insert(END, data)
    
    elif filtrado.get() == "85 - 90":
        listbox.delete(0,END)
        secondaryDf = df[df['Edad'].between(85, 90)]
        shownData = list(secondaryDf[['id', 'Nombre', 'Edad']].values)
        listbox.insert(END, "[id, Nombre]")
        for data in shownData:
            listbox.insert(END, '---------------------------------------------')
            listbox.insert(END, data)

lst = ['Edad', 'Ocupacion']

lst2 = ['15 - 44', '45 - 84', '85 - 90']
mw = tk.Tk()
filtroSec = filtradoSecundario = ttk.Combobox(mw,value=lst2)
btnSec = btnFiltradoSecundario = tk.Button(text='Filtrar edad', command=lambda: filtrarSecundario(filtradoSecundario))
mw.title('Usuarios')
mw.geometry("500x500") 
mw.resizable(0, 0)
 
filtradoPrincipal = ttk.Combobox(mw,value=lst)
filtradoPrincipal.set('Filtrado')
filtradoPrincipal.place(x = 78, y = 15)

btnFiltradoPrincipal = tk.Button(text='Filtrar', command=filtrarPrincipal)
btnFiltradoPrincipal.place(x = 100, y = 45, width=100, height=25)


listbox = tk.Listbox(mw)
listbox.grid(padx = 50, pady= 75)
listbox.config(width=65, height=20)
 
mw.mainloop()