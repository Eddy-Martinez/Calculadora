from tkinter import *
global entrada
global variable1
global variable2
global bandera
variable1=0
variable2=0
entrada=0
bandera=0
def uno():
    global entrada
    entrada=entrada*10+1
    l1=Label(ventana,text=entrada,font=("arial 15")).grid(column=0,row=0)
def dos():
    global entrada
    entrada=entrada*10+2
    l2=Label(ventana,text=entrada,font=("arial 15")).grid(column=0,row=0)
def tres():
    global entrada
    entrada=entrada*10+3
    l3=Label(ventana,text=entrada,font=("arial 15")).grid(column=0,row=0)
def cuatro():
    global entrada
    entrada=entrada*10+4
    l4=Label(ventana,text=entrada,font=("arial 15")).grid(column=0,row=0)
def cinco():
    global entrada
    entrada=entrada*10+5
    l5=Label(ventana,text=entrada,font=("arial 15")).grid(column=0,row=0)
def seis():
    global entrada
    entrada=entrada*10+6
    l6=Label(ventana,text=entrada,font=("arial 15")).grid(column=0,row=0)
def siete():
    global entrada
    entrada=entrada*10+7
    l7=Label(ventana,text=entrada,font=("arial 15")).grid(column=0,row=0)
def ocho():
    global entrada
    entrada=entrada*10+8
    l8=Label(ventana,text=entrada,font=("arial 15")).grid(column=0,row=0)
def nueve():
    global entrada
    entrada=entrada*10+9
    l9=Label(ventana,text=entrada,font=("arial 15")).grid(column=0,row=0)
def cero():
    global entrada
    entrada=entrada*10+0
    l0=Label(ventana,text=entrada,font=("arial 15")).grid(column=0,row=0)
    
def suma():
    global entrada
    global variable1
    global bandera
    variable1=entrada
    entrada=0
    bandera=1
    
def resta():
    global entrada
    global variable1
    global bandera
    variable1=entrada
    entrada=0
    bandera=2
    
def multiplicacion():
    global entrada
    global variable1
    global bandera
    variable1=entrada
    entrada=0
    bandera=3
    
def division():
    global entrada
    global variable1
    global bandera
    variable1=entrada
    entrada=0
    bandera=4
    
        
def igual():
    if(bandera==1):
        variable2=variable1+entrada
    if(bandera==2):
        variable2=variable1-entrada
    if(bandera==3):
        variable2=variable1*entrada
    if(bandera==4):
        try:
            variable2=variable1/entrada
        except ZeroDivisionError:
            variable2=Label(ventana,text="error",font=("arial 15")).grid(column=3,row=0)
    Label(ventana,text="=",font=("arial 15")).grid(column=1,row=0)
    Label(ventana,text=(variable2),font=("arial 15")).grid(column=2,row=0)
def clear():
    entrada=0
    variable1=0
    variable2=0
    bandera=0
    Label(ventana,text=entrada,font=("arial 15")).grid(column=0,row=0)
    Label(ventana,text=entrada,font=("arial 15")).grid(column=5,row=5)
        
ventana=Tk()
b1=Button(ventana,text="+",font=("arial 15"),command=suma).grid(column=4,row=1)
b2=Button(ventana,text="-",font=("arial 15"),command=resta).grid(column=4,row=2)
b3=Button(ventana,text="x",font=("arial 15"),command=multiplicacion).grid(column=4,row=3)
b4=Button(ventana,text="/",font=("arial 15"),command=division).grid(column=4,row=4)

b5=Button(ventana,text="1",font=("arial 15"),command=uno).grid(column=1,row=1)
b6=Button(ventana,text="2",font=("arial 15"),command=dos).grid(column=2,row=1)
b7=Button(ventana,text="3",font=("arial 15"),command=tres).grid(column=3,row=1)

b8=Button(ventana,text="4",font=("arial 15"),command=cuatro).grid(column=1,row=2)
b9=Button(ventana,text="5",font=("arial 15"),command=cinco).grid(column=2,row=2)
b10=Button(ventana,text="6",font=("arial 15"),command=seis).grid(column=3,row=2)

b11=Button(ventana,text="7",font=("arial 15"),command=siete).grid(column=1,row=3)
b12=Button(ventana,text="8",font=("arial 15"),command=ocho).grid(column=2,row=3)
b13=Button(ventana,text="9",font=("arial 15"),command=nueve).grid(column=3,row=3)
b14=Button(ventana,text="0",font=("arial 15"),command=cero).grid(column=2,row=4)

b15=Button(ventana,text="=",font=("arial 15"),command=igual).grid(column=3,row=4)
b16=Button(ventana,text="clr",font=("arial 15"),command=clear).grid(column=1,row=4)

ventana.mainloop()
