from tkinter import *

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("310x260")

# Configuración pantalla de salida 
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=40, padx=1, pady=1)

# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_1.grid(row=1, column=0, padx=0, pady=1)

boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_2.grid(row=1, column=1, padx=0, pady=1)

boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_3.grid(row=1, column=2, padx=0, pady=1)

boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_4.grid(row=2, column=0, padx=1, pady=1)

boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_5.grid(row=2, column=1, padx=1, pady=1)

boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_6.grid(row=2, column=2, padx=1, pady=1)

boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_7.grid(row=3, column=0, padx=1, pady=1)

boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_8.grid(row=3, column=1, padx=1, pady=1)

boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_9.grid(row=3, column=2, padx=1, pady=1)

boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2")
boton_igual.grid(row=4, column=0, columnspan=2, padx=1, pady=1)

boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0)
boton_punto.grid(row=4, column=2, padx=1, pady=1)

boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_mas.grid(row=1, column=3, padx=1, pady=1)

boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_menos.grid(row=2, column=3, padx=1, pady=1)

boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_multiplicacion.grid(row=3, column=3, padx=1, pady=1)

boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_division.grid(row=4, column=3, padx=1, pady=1)

#Funcionalidad
i = 0 

def getNumbers(n):
    global i
    pantalla.insert(i,n)
    i+=1 

def getOperators(n):
    global i
    pantalla.insert(i,n)
    i+=1

boton_1.bind("<Button>", lambda x:getNumbers(1))
boton_2.bind("<Button>", lambda x: getNumbers(2))
boton_3.bind("<Button>", lambda x: getNumbers(3))
boton_4.bind("<Button>", lambda x: getNumbers(4))
boton_5.bind("<Button>", lambda x: getNumbers(5))
boton_6.bind("<Button>", lambda x: getNumbers(6))
boton_7.bind("<Button>", lambda x: getNumbers(7))
boton_8.bind("<Button>", lambda x: getNumbers(8))
boton_9.bind("<Button>", lambda x: getNumbers(9))

boton_mas.bind("<Button>", lambda x: getOperators("+"))
boton_menos.bind("<Button>", lambda x: getOperators("-"))
boton_multiplicacion.bind("<Button>", lambda x: getOperators("*"))
boton_division.bind("<Button>", lambda x: getOperators("/"))
boton_punto.bind("<Button>", lambda x: getOperators("."))
boton_igual.bind("<Button>",lambda x: calculate())


def calculate():
    operacion = pantalla.get()
    pantalla.delete(0,END)

    if (operacion.find("+")!=-1):
        indexN1 = operacion.find("+")
        N1= float(operacion[0:indexN1])
        N2= float(operacion[indexN1+1:])
        pantalla.insert(END,str(N1+N2))

    elif (operacion.find("-")!=-1):
        indexN1 = operacion.find("-")
        N1= float(operacion[0:indexN1])
        N2= float(operacion[indexN1+1:])
        pantalla.insert(END,str(N1-N2))
    
    elif (operacion.find("*")!=-1):
        indexN1 = operacion.find("*")
        N1= float(operacion[0:indexN1])
        N2= float(operacion[indexN1+1:])
        pantalla.insert(END,str(N1*N2))

    elif (operacion.find("/")!=-1):
        indexN1 = operacion.find("/")
        N1= float(operacion[0:indexN1])
        N2= float(operacion[indexN1+1:])
        pantalla.insert(END,str(N1/N2))

#final vr

root.mainloop()