import tkinter as tk
from tkinter import END, ttk
from tkinter.ttk import *
import pandas as pd
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(True)

df = pd.read_csv('usuarios.txt')

def on_field_change():
    if comboboxMainFilter.get() == "Edad":
        secFilter.set('Filtrado por edad')
        secFilter.place(x = 340, y = 15)
        btnSec.place(x = 380, y = 45, width=100, height=25)
    
    else:
        secFilter.place_forget()
        btnSec.place_forget()
    
def functionMainFilter(columna):
    listboxData.delete(0,END)
    shownData = list(df[['id','Nombre', columna]].values)
    for data in shownData:
        listboxData.insert(END, '---------------------------------------------')
        listboxData.insert(END, ("ID: "+str(data[0])), ("Nombre: "+str(data[1])), (columna+": "+str(data[2])))

def functionSecondaryFilter(min, max):
    listboxData.delete(0,END)
    secondaryDf = df[df['Edad'].between(min, max)]
    shownData = list(secondaryDf[['id', 'Nombre', 'Edad']].values)
    for data in shownData:
        listboxData.insert(END, '---------------------------------------------')
        listboxData.insert(END, ("ID: "+str(data[0])), ("Nombre: "+str(data[1])), ("Edad: "+str(data[2])))

def mainFilter():
    on_field_change()
    if comboboxMainFilter.get() == "Edad":
        functionMainFilter('Edad')
    
    elif comboboxMainFilter.get() == "Ocupación":
        functionMainFilter('Ocupación')

def secondaryFilter(filtrado):
    if filtrado.get() == "15 - 44":
        functionSecondaryFilter(15, 44)
    
    elif filtrado.get() == "45 - 84":
        functionSecondaryFilter(45, 84)
    
    elif filtrado.get() == "85 - 90":
        functionSecondaryFilter(85, 90)

def statistics():
    on_field_change()
    if comboboxMainFilter.get() == "Edad":
        listboxData.delete(0,END)
        shownData = dict(df['Edad'].value_counts(sort=True))
        for key, value in shownData.items():
            listboxData.insert(END, '--------------------------------------------------------')
            listboxData.insert(END, ("Edad: "+str(key)), ("Cantidad de personas con esta edad: "+str(value)), ("Porcentaje de personas con esta edad: "+str(value*100/1000)+"%"))
    
    elif comboboxMainFilter.get() == "Ocupación":
        listboxData.delete(0,END)
        shownData = dict(df['Ocupación'].value_counts(ascending=True))
        for key, value in shownData.items():
            listboxData.insert(END, '--------------------------------------------------------')
            listboxData.insert(END, ("Ocupación: "+str(key)), ("Cantidad de personas con esta ocupación: "+str(value)), ("Porcentaje de personas con esta ocupación: "+str(value*100/1000)+"%"))

filterList = ['Edad', 'Ocupación']

secFilterList = ['15 - 44', '45 - 84', '85 - 90']
mw = tk.Tk()
secFilter = comboboxSecondaryFilter = ttk.Combobox(mw,value=secFilterList)
btnSec = btnSecondaryFilter = tk.Button(text='Filtrar edad', command=lambda: secondaryFilter(comboboxSecondaryFilter))
mw.title('Usuarios')
mw.geometry("600x600") 
mw.resizable(0, 0)
 
comboboxMainFilter = ttk.Combobox(mw,value=filterList)
comboboxMainFilter.set('Filtrado')
comboboxMainFilter.place(x = 78, y = 15)

btnMainFilter = tk.Button(text='Filtrar', command=mainFilter)
btnMainFilter.place(x = 120, y = 45, width=100, height=25)

btnStatistics = tk.Button(text='Obtener estadísticas', command=statistics)
btnStatistics.place(x = 240, y = 520, width=160, height=30)

listboxData = tk.Listbox(mw)
listboxData.grid(padx = 50, pady= 75)
listboxData.config(width=65, height=20)
 
mw.mainloop()