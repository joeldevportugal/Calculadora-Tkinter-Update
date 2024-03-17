from tkinter import *

def clear():
    EEcra.delete(0, END)

def button_click(number):
    current = EEcra.get()
    EEcra.delete(0, END)
    EEcra.insert(0, str(current) + str(number))

def soma():
    first_number = EEcra.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    EEcra.delete(0, END)

def subtrair():
    first_number = EEcra.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    EEcra.delete(0, END)

def Multiplicar():
    first_number = EEcra.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    EEcra.delete(0, END)

def dividir():
    first_number = EEcra.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    EEcra.delete(0, END)

def igual():
    second_number = EEcra.get()
    EEcra.delete(0, END)
    if math == "addition":
        EEcra.insert(0, f_num + float(second_number))
    elif math == "subtraction":
        EEcra.insert(0, f_num - float(second_number))
    elif math == "multiplication":
        EEcra.insert(0, f_num * float(second_number))
    elif math == "division":
        EEcra.insert(0, f_num / float(second_number))

def button_percent():
    first_number = EEcra.get()
    EEcra.delete(0, END)
    EEcra.insert(0, float(first_number) / 100)

def button_backspace():
    current = EEcra.get()
    EEcra.delete(len(current) - 1, END)

def button_decimal():
    current = EEcra.get()
    if "." not in current:
        EEcra.insert(END, ".")

# Funções da Memória
memoria = []

def adicionar_memoria(valor):
    memoria.append(valor)

def recuperar_memoria():
    if memoria:
        valor = memoria[-1]
        EEcra.delete(0, END)
        EEcra.insert(END, str(valor))

def limpar_memoria():
    memoria.clear()

# defenir as Cores a Usar --------------------------------------------------------
co1='#FFFFFF'
co2='#B2AAB3'
co3='#F0F6F3'
co4='#FFFFFF'
#---------------------------------------------------------------------------------
# configurar a Nossa Janela
janela = Tk()
janela.geometry('290x250+100+100')
janela.resizable(False, False)
janela.title('Calc Dev Joel PT © 24')
janela.config(bg=co1)
janela.iconbitmap('C:\\Users\\HP\\Desktop\\Projectos\\Calculadora\\icon.ico')

# criar Todo O frontend
EEcra = Entry(janela, bg=co3, font=('Arial 14'), width=24, justify=RIGHT)
EEcra.place(x=10, y=5)
BMEM = Button(janela, text="MEM", bg=co2,fg=co4,font=('Arial 11 bold'), width=14, relief=RAISED, overrelief=RIDGE, command=recuperar_memoria)
BMEM.place(x=10, y=35)
Bclear = Button(janela, text="C", bg=co2,fg=co4,font=('Arial 11 bold'), width=13, relief=RAISED, overrelief=RIDGE, command=clear)
Bclear.place(x=150, y=35)
BModulo = Button(janela, text='%', bg=co2,fg=co4,font=('Arial 11 bold '), width=6, relief=RAISED, overrelief=RIDGE, command=button_percent)
BModulo.place(x=10, y=70)
BMul = Button(janela, text='X', bg=co2,fg=co4,font=('Arial 11 bold'), width=6, relief=RAISED, overrelief=RIDGE, command=Multiplicar)
BMul.place(x=80, y=70)
BDiv = Button(janela, text='/', bg=co2,fg=co4,font=('Arial 11 bold'), width=6, relief=RAISED, overrelief=RIDGE, command=dividir)
BDiv.place(x=150, y=70)
BBack = Button(janela, text='←',bg=co2, fg=co4,font=('Arial 11 bold'), width=5, relief=RAISED, overrelief=RIDGE, command=button_backspace)
BBack.place(x=220, y=70)
BSete = Button(janela, text='7', bg=co2, fg=co4, font=('Arial 11 bold'), width=6, relief=RAISED, overrelief=RIDGE, command=lambda: button_click(7))
BSete.place(x=10, y=105)
BOito = Button(janela, text='8', bg=co2, fg=co4, font=('Arial 11 bold'), width=6, relief=RAISED, overrelief=RIDGE, command=lambda: button_click(8))
BOito.place(x=80, y=105)
BNove = Button(janela, text='9', bg=co2, fg=co4, font=('Arial 11 bold'), width=6, relief=RAISED, overrelief=RIDGE, command=lambda: button_click(9))
BNove.place(x=150, y=105)
BSub = Button(janela, text='-', bg=co2, fg=co4, font=('Arial 11 bold'), width=5, relief=RAISED, overrelief=RIDGE, command=subtrair)
BSub.place(x=220, y=105)
BQuatro = Button(janela, text='4', bg=co2, fg=co4, font=('Arial 11 bold'), width=6, relief=RAISED, overrelief=RIDGE, command=lambda: button_click(4))
BQuatro.place(x=10, y=140)
BCinco = Button(janela, text='5', bg=co2, fg=co4, font=('Arial 11 bold'), width=6, relief=RAISED, overrelief=RIDGE, command=lambda: button_click(5))
BCinco.place(x=80, y=140)
BSeis = Button(janela, text='6', bg=co2, fg=co4, font=('Arial 11 bold'), width=6, relief=RAISED, overrelief=RIDGE, command=lambda: button_click(6))
BSeis.place(x=150, y=140)
BSoma = Button(janela, text='+', bg=co2, fg=co4,font=('Arial 11 bold'), width=5, height=5, relief=RAISED, overrelief=RIDGE, command=soma)
BSoma.place(x=220, y=140)
BUM = Button(janela, text='1', bg=co2, fg=co4,font=('Arial 11 bold'), width=6, relief=RAISED, overrelief=RIDGE, command=lambda: button_click(1))
BUM.place(x=10, y=175)
BDois = Button(janela, text='2', bg=co2, fg=co4, font=('Arial 11 bold'), width=6, relief=RAISED, overrelief=RIDGE, command=lambda: button_click(2))
BDois.place(x=80, y=175)
BTres = Button(janela, text='3', bg=co2, fg=co4,font=('Arial 11 bold'), width=6, relief=RAISED, overrelief=RIDGE, command=lambda: button_click(3))
BTres.place(x=150, y=175)
BZero = Button(janela, text='0', bg=co2, fg=co4,font=('Arial 11 bold'), width=6, height=1, relief=RAISED, overrelief=RIDGE, command=lambda: button_click(0))
BZero.place(x=10, y=212)
BDecimal = Button(janela, text=',', bg=co2, fg=co4, font=('Arial 11 bold'), width=6, height=1, relief=RAISED, overrelief=RIDGE, command=button_decimal)
BDecimal.place(x=80, y=212)
Bigual = Button(janela, text='=', bg=co2, fg=co4, font=('Arial 11 bold'), width=6, height=1, relief=RAISED, overrelief=RIDGE, command=igual)
Bigual.place(x=150, y=212)

janela.mainloop()
