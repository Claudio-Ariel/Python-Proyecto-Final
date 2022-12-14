import tkinter as tk
import tkinter.font as tkFont

class Sala(tk.Toplevel):
    def __init__(self, master = None, sala_id =  None):
        super().__init__(master)
        self.master = master
        self.sala_id = sala_id
        #setting title
        self.title("Registro de Productos")
        #setting window size
        width=350
        height=350
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_986=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_986["font"] = ft
        GLabel_986["fg"] = "#333333"
        GLabel_986["justify"] = "left"
        GLabel_986["text"] = "Producto:"
        GLabel_986.place(x=10,y=10,width=70,height=25)

        GLabel_949=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_949["font"] = ft
        GLabel_949["fg"] = "#333333"
        GLabel_949["justify"] = "left"
        GLabel_949["text"] = "Marca:"
        GLabel_949.place(x=10,y=50,width=70,height=25)

        GLabel_205=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_205["font"] = ft
        GLabel_205["fg"] = "#333333"
        GLabel_205["justify"] = "left"
        GLabel_205["text"] = "Stock:"
        GLabel_205.place(x=10,y=90,width=70,height=25)

        GLabel_205=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_205["font"] = ft
        GLabel_205["fg"] = "#333333"
        GLabel_205["justify"] = "left"
        GLabel_205["text"] = "Tipo:"
        GLabel_205.place(x=10,y=130,width=70,height=25)

        GLabel_205=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_205["font"] = ft
        GLabel_205["fg"] = "#333333"
        GLabel_205["justify"] = "left"
        GLabel_205["text"] = "Codigo:"
        GLabel_205.place(x=10,y=170,width=70,height=25)

        GLabel_205=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_205["font"] = ft
        GLabel_205["fg"] = "#333333"
        GLabel_205["justify"] = "left"
        GLabel_205["text"] = "Precio:"
        GLabel_205.place(x=10,y=210,width=70,height=25)

        
        GLineEdit_119=tk.Entry(self, name = "txtProducto")
        GLineEdit_119["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_119["font"] = ft
        GLineEdit_119["fg"] = "#333333"
        GLineEdit_119["justify"] = "left"
        GLineEdit_119["text"] = ""
        GLineEdit_119.place(x=80,y=10,width=250,height=30)

        GLineEdit_522=tk.Entry(self, name = "txtMarca")
        GLineEdit_522["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_522["font"] = ft
        GLineEdit_522["fg"] = "#333333"
        GLineEdit_522["justify"] = "left"
        GLineEdit_522["text"] = ""
        GLineEdit_522.place(x=80,y=50,width=250,height=30)

        GLineEdit_557=tk.Entry(self, name = "txtStock")
        GLineEdit_557["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_557["font"] = ft
        GLineEdit_557["fg"] = "#333333"
        GLineEdit_557["justify"] = "left"
        GLineEdit_557["text"] = ""
        GLineEdit_557.place(x=80,y=90,width=250,height=30)

        GLineEdit_557=tk.Entry(self, name = "txtTipo")
        GLineEdit_557["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_557["font"] = ft
        GLineEdit_557["fg"] = "#333333"
        GLineEdit_557["justify"] = "left"
        GLineEdit_557["text"] = ""
        GLineEdit_557.place(x=80,y=130,width=250,height=30)

        GLineEdit_557=tk.Entry(self, name = "txtCodigo")
        GLineEdit_557["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_557["font"] = ft
        GLineEdit_557["fg"] = "#333333"
        GLineEdit_557["justify"] = "left"
        GLineEdit_557["text"] = ""
        GLineEdit_557.place(x=80,y=170,width=250,height=30)

        GLineEdit_557=tk.Entry(self, name = "txtPrecio")
        GLineEdit_557["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_557["font"] = ft
        GLineEdit_557["fg"] = "#333333"
        GLineEdit_557["justify"] = "left"
        GLineEdit_557["text"] = ""
        GLineEdit_557.place(x=80,y=210,width=250,height=30)
       
        GButton_215=tk.Button(self)
        GButton_215["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_215["font"] = ft
        GButton_215["fg"] = "#000000"
        GButton_215["justify"] = "center"
        GButton_215["text"] = "Aceptar"
        GButton_215.place(x=100,y=310,width=70,height=25)
        GButton_215["command"] = self.aceptar

        GButton_901=tk.Button(self)
        GButton_901["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_901["font"] = ft
        GButton_901["fg"] = "#000000"
        GButton_901["justify"] = "center"
        GButton_901["text"] = "Cancelar"
        GButton_901.place(x=180,y=310,width=70,height=25)
        GButton_901["command"] = self.cancelar

    def aceptar(self):
        producto = self.get_value("txtProducto")
        marca = self.get_value("txtMarca")
        stock = self.get_value("txtStock")
        tipo = self.get_value("txtTipo")
        codigo = self.get_value("txtCodigo")
        precio = self.get_value("txtPrecio")
        print(producto, marca, stock, tipo, codigo, precio)
        #validar datos
        #fijarme si es una alta o es una edicion
        if self.sala_id is None:
            print("alta nueva de sala")
            #guardar los datos en la bd
        else:
            print("edicion de sala")
            #guardar los datos en la bd       


    def cancelar(self):
        self.destroy()

    def get_value(self, name):
        return self.nametowidget(name).get()
