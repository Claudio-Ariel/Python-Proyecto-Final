import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
class App:
    def __init__(self, root):
        #setting title
        root.title("CARRITO DE COMPRAS - SUPERMARK QUE PRECIOS")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_954=tk.Button(root)
        GButton_954["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_954["font"] = ft
        GButton_954["fg"] = "#000000"
        GButton_954["justify"] = "center"
        GButton_954["text"] = "COMPRAR"
        GButton_954.place(x=300,y=450,width=70,height=25)
        GButton_954["command"] = self.GButton_954_command

        GLineEdit_970=tk.Entry(root)
        GLineEdit_970["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_970["font"] = ft
        GLineEdit_970["fg"] = "#333333"
        GLineEdit_970["justify"] = "center"
        GLineEdit_970["text"] = "Entry"
        GLineEdit_970.place(x=450,y=120,width=107,height=30)

        GLabel_890=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_890["font"] = ft
        GLabel_890["fg"] = "#333333"
        GLabel_890["justify"] = "center"
        GLabel_890["text"] = "         Añade al carrito los productos que deseas comprar"
        GLabel_890.place(x=20,y=70,width=372,height=30)

        GLabel_353=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_353["font"] = ft
        GLabel_353["fg"] = "#333333"
        GLabel_353["justify"] = "center"
        GLabel_353["text"] = "Ingrese el codigo del producto elegido separados por coma (,)"
        GLabel_353.place(x=60,y=110,width=357,height=45)

        GLabel_663=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_663["font"] = ft
        GLabel_663["fg"] = "#333333"
        GLabel_663["justify"] = "center"
        GLabel_663["text"] = ""
        GLabel_663.place(x=60,y=140,width=70,height=25)

        GLabel_233=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_233["font"] = ft
        GLabel_233["fg"] = "#333333"
        GLabel_233["justify"] = "center"
        GLabel_233["text"] = "Siguiendo el orden ingresado, indique las unidades por producto"
        GLabel_233.place(x=60,y=190,width=367,height=30)

        GLineEdit_153=tk.Entry(root)
        GLineEdit_153["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_153["font"] = ft
        GLineEdit_153["fg"] = "#333333"
        GLineEdit_153["justify"] = "center"
        GLineEdit_153["text"] = "Entry"
        GLineEdit_153.place(x=450,y=190,width=105,height=30)

        GButton_921=tk.Button(root)
        GButton_921["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_921["font"] = ft
        GButton_921["fg"] = "#000000"
        GButton_921["justify"] = "center"
        GButton_921["text"] = "CANCELAR"
        GButton_921.place(x=410,y=450,width=70,height=25)
        GButton_921["command"] = self.GButton_921_command
        
        GLabel_913=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_913["font"] = ft
        GLabel_913["fg"] = "#333333"
        GLabel_913["justify"] = "center"
        GLabel_913["text"] = "Detalle de su compra"
        GLabel_913.place(x=50,y=320,width=148,height=30)

        GLabel_967=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_967["font"] = ft
        GLabel_967["fg"] = "#333333"
        GLabel_967["justify"] = "center"
        GLabel_967["text"] = "Total a pagar"
        GLabel_967.place(x=40,y=390,width=125,height=30)

        GLabel_230=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_230["font"] = ft
        GLabel_230["fg"] = "#333333"
        GLabel_230["justify"] = "center"
        GLabel_230["text"] = "BIENVENIDOS A SU SISTEMA DE VENTAS ONLINE FAVORITO"
        GLabel_230.place(x=120,y=30,width=377,height=30)

        GButton_550=tk.Button(root)
        GButton_550["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_550["font"] = ft
        GButton_550["fg"] = "#000000"
        GButton_550["justify"] = "center"
        GButton_550["text"] = "AGREGAR PRODUCTO"
        GButton_550.place(x=90,y=270,width=134,height=31)
        GButton_550["command"] = self.GButton_550_command

        GButton_597=tk.Button(root)
        GButton_597["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_597["font"] = ft
        GButton_597["fg"] = "#000000"
        GButton_597["justify"] = "center"
        GButton_597["text"] = "BORRAR PRODUCTO"
        GButton_597.place(x=440,y=270,width=132,height=31)
        GButton_597["command"] = self.GButton_597_command

        GButton_133=tk.Button(root)
        GButton_133["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_133["font"] = ft
        GButton_133["fg"] = "#000000"
        GButton_133["justify"] = "center"
        GButton_133["text"] = "MODIFICAR PRODUCTO"
        GButton_133.place(x=260,y=270,width=142,height=31)
        GButton_133["command"] = self.GButton_133_command

    def GButton_954_command(self):
        print("command")


    def GButton_921_command(self):
        print("command")


    def GButton_550_command(self):
        print("command")


    def GButton_597_command(self):
        print("command")


    def GButton_133_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

def agregar_item(self, producto, precio):
    """Agrega un producto al carrito."""
    self.producto = producto
    self.precio = precio