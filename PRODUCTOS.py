from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMsgBox
import tkinter as tk
import tkinter.font as tkFont

class Producto(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        #setting title
        self.title("Listado de Productos")
        #setting window size
        width=497
        height=439
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GButton_779=tk.Button(self)
        GButton_779["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_779["font"] = ft
        GButton_779["fg"] = "#000000"
        GButton_779["justify"] = "center"
        GButton_779["text"] = "Editar"
        GButton_779.place(x=310,y=10,width=70,height=25)
        GButton_779["command"] = self.Editar

        GButton_171=tk.Button(self)
        GButton_171["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_171["font"] = ft
        GButton_171["fg"] = "#000000"
        GButton_171["justify"] = "center"
        GButton_171["text"] = "Eliminar"
        GButton_171.place(x=390,y=10,width=70,height=25)
        GButton_171["command"] = self.Eliminar

        GButton_731=tk.Button(self)
        GButton_731["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_731["font"] = ft
        GButton_731["fg"] = "#000000"
        GButton_731["justify"] = "center"
        GButton_731["text"] = "Agregar"
        GButton_731.place(x=230,y=10,width=70,height=25)
        GButton_731["command"] = self.Agregar

        GLabel_795=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_795["font"] = ft
        GLabel_795["fg"] = "#333333"
        GLabel_795["justify"] = "center"
        GLabel_795["text"] = "Id_Prod"
        GLabel_795.place(x=0,y=50,width=70,height=25)

        GLabel_27=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_27["font"] = ft
        GLabel_27["fg"] = "#333333"
        GLabel_27["justify"] = "center"
        GLabel_27["text"] = "Nombre"
        GLabel_27.place(x=70,y=50,width=70,height=25)

        GLabel_875=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_875["font"] = ft
        GLabel_875["fg"] = "#333333"
        GLabel_875["justify"] = "center"
        GLabel_875["text"] = "Marca"
        GLabel_875.place(x=140,y=50,width=70,height=25)

        GLabel_955=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_955["font"] = ft
        GLabel_955["fg"] = "#333333"
        GLabel_955["justify"] = "center"
        GLabel_955["text"] = "Stock"
        GLabel_955.place(x=210,y=50,width=70,height=25)

        GLabel_33=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_33["font"] = ft
        GLabel_33["fg"] = "#333333"
        GLabel_33["justify"] = "center"
        GLabel_33["text"] = "Productos"
        GLabel_33.place(x=10,y=10,width=137,height=30)

        GLabel_74=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_74["font"] = ft
        GLabel_74["fg"] = "#333333"
        GLabel_74["justify"] = "center"
        GLabel_74["text"] = "Tipo"
        GLabel_74.place(x=280,y=50,width=70,height=25)

        GLabel_962=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_962["font"] = ft
        GLabel_962["fg"] = "#333333"
        GLabel_962["justify"] = "center"
        GLabel_962["text"] = "Codigo"
        GLabel_962.place(x=350,y=50,width=70,height=25)

        GLabel_242=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_242["font"] = ft
        GLabel_242["fg"] = "#333333"
        GLabel_242["justify"] = "center"
        GLabel_242["text"] = "Precio"
        GLabel_242.place(x=420,y=50,width=70,height=25)

    def Editar(self):
        print("Editar")


    def Eliminar(self):
        print("Eliminar")


    def Agregar(self):
        print("Agregar")


